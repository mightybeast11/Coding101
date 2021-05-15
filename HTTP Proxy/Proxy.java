import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.nodes.TextNode;
import org.jsoup.select.Elements;

import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Date;
import java.util.List;

public class Proxy {
    final static int PORT = 6331;
    static int text_changes = 0;
    static int link_rewrites = 0;

    private static String replace(String text, String city, String target) {
        while (text.contains(city)) {
            text = text.replace(city, target);
            text_changes++;
        }
        return text;
    }

    private static String modifyText(String text) {
        text = replace(text, "Canberra", "CCCC");
        text = replace(text, "Sydney", "SSSS");
        text = replace(text, "Darwin", "DDDD");
        text = replace(text, "Brisbane", "BBBB");
        text = replace(text, "Adelaide", "AAAA");
        text = replace(text, "Hobart", "HHHH");
        text = replace(text, "Melbourne", "MMMM");
        text = replace(text, "Perth", "PPPP");
        return text;
    }

    private static void sendResponse(URL url, String relativePath, DataOutputStream to_browser) throws IOException {
        // connect to remote server
        Socket remoteSocket = new Socket(InetAddress.getByName(url.getHost()), 80);
        System.out.println("Proxy Client: created socket connected to local port " + remoteSocket.getLocalPort() +
                " and to remote address " + remoteSocket.getInetAddress() +
                " port " + remoteSocket.getPort());
        DataInputStream from_website = new DataInputStream(remoteSocket.getInputStream());
        DataOutputStream to_website = new DataOutputStream(remoteSocket.getOutputStream());

        // send request to remote
        PrintWriter pw = new PrintWriter(to_website);
        String request = "GET " + relativePath + " HTTP/1.0\r\n";
        pw.print(request);
        pw.print("User-Agent: wzh\r\n");
        pw.print("Host: www.bom.gov.au\r\n");
        pw.print("\r\n");
        pw.flush();
        System.out.println(new Date() + ": " + request.trim()); // log request with timestamp

        // get response from remote, send response to browser
        byte[] remoteResponse = new byte[131072]; // smaller capacity can lead to incomplete webpage
        int bytes_read;
        try {
            while ((bytes_read = from_website.read(remoteResponse)) != -1) {
                String responseString = new String(remoteResponse, StandardCharsets.UTF_8);
                // modify absolute links
                while (responseString.contains(url.toString())) {
                    responseString = responseString.replaceAll(url.toString(), "");
                    link_rewrites++;
                }
                String[] responseLines = responseString.split("\r\n");
                responseString = null; // gc
                if (responseLines[0].contains("HTTP/1.0")) {
                    System.out.println(new Date() + ": " + responseLines[0]); // log response with timestamp
                }

                if (responseLines[responseLines.length-1].contains("<")) {
                    // parse and modify displayed texts
                    Document doc = Jsoup.parseBodyFragment(responseLines[responseLines.length-1]);
                    Elements elements = doc.body().getAllElements();
                    for (Element element : elements) {
                        List<TextNode> textnodeList = element.textNodes();
                        for (TextNode textnode : textnodeList){
                            String text = textnode.text();
                            textnode.text(modifyText(text));
                        }
                    }
                    // add header back, convert to byte
                    String htmlString = doc.body().toString();
                    doc = null; // gc
                    elements = null; // gc
                    StringBuilder modifiedString = new StringBuilder();
                    for (int i = 0; i < responseLines.length-1; i++) {
                        modifiedString.append(responseLines[i]).append("\r\n");
                    }
                    responseLines = null; // gc
                    modifiedString.append("\r\n");
                    modifiedString.append(htmlString);
                    byte[] modifiedResponse = modifiedString.toString().getBytes(StandardCharsets.UTF_8);
                    modifiedString = null; // gc
                    to_browser.write(modifiedResponse, 0, modifiedResponse.length);
                    modifiedResponse = null; // gc
                }
                else {
                    to_browser.write(remoteResponse, 0, bytes_read);
                }
                to_browser.flush();
            }
            remoteResponse = null; // gc
        } catch (IOException e) {
            System.out.println(e);
        }
        remoteSocket.close();
    }

    public static void main(String[] args) throws IOException {
        // input URL validity check
        URL url = null;
        if (args.length == 1) {
            url = new URL(args[0]);
            try {
                url.toURI();
            } catch (URISyntaxException e) {
                System.out.println("Input URL is invalid.");
                System.exit(1);
            }
        } else {
            System.out.println("Command line argument is invalid.");
            System.exit(1);
        }

        // open localhost server
        ServerSocket proxyServerSocket = new ServerSocket(PORT);
        System.out.println("Proxy Server: created socket with port " + proxyServerSocket.getLocalPort() + "\n");

        // infinite loop: listen to browser for further requests
        while (true) {
            text_changes = 0; // reset for new webpage
            link_rewrites = 0; // reset for new webpage

            // point browser at localhost:PORT
            Socket localSocket = proxyServerSocket.accept(); // each browser request could be on different port, so accept() must be inside loop
            System.out.println("Proxy Server: received connection from " + localSocket.getRemoteSocketAddress() + ", " +
                    "now on port " + localSocket.getLocalPort());

            // prepare streams between proxy server and browser
            DataInputStream from_browser = new DataInputStream(localSocket.getInputStream());
            DataOutputStream to_browser = new DataOutputStream(localSocket.getOutputStream());

            // get request from browser
            final byte[] browser_request = new byte[8192];
            try {
                while (from_browser.read(browser_request) != -1) {
                    // parse browser request
                    String str = new String(browser_request, StandardCharsets.UTF_8);
                    String[] requestLines = str.split("\r\n");
                    String path = requestLines[0].split(" ")[1];
                    System.out.println("Path: " + path);
                    sendResponse(url, path, to_browser);
                }
            } catch (IOException e) {
                System.out.println(e);
            }

            System.out.println("Text changes: " + text_changes); // log number of text changes
            System.out.println("Link changes: " + link_rewrites + "\n"); // log number of link changes
            localSocket.close();
        }
    }
}
