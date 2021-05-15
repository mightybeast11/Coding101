# Setup in IntelliJ (Recommended)

-   Create a new project with IntelliJ IDEA with this folder. (1 java file, 1 jar file, 1 md file)
-   Add `jsoup-1.31.1.jar` file into project library. 

-   Add URL string as `main` method argument following this [instruction](https://stackoverflow.com/questions/2066307/how-do-you-input-command-line-arguments-in-intellij-idea). For the default website, input "http://www.bom.gov.au" into the **Program Arguments** field. (Note: URL argument only supports **one single string url**.)
-   Run `Proxy.java` in IntelliJ.
-   Input `localhost:6331` in a browser to retrieve the modified main page. Enjoy marking!

---

# Setup in command line (Not recommended)

This approach is not recommended, because it is tricky to compile with external library (jsoup) in command line. The `javac` command syntax seems to be different across operating systems.

-   Run `javac` to compile, including jsoup in class path:

    `javac -classpath ".:/home/path/jsoup-1.31.1.jar" Proxy.java`

    The path "/home/path/jsoup.jar" should be replaced with you local path of the jar file. This is the [source](https://stackoverflow.com/questions/9395207/how-to-include-jar-files-with-java-file-and-compile-in-command-prompt) for this syntax, but it does not work on macOS.

-   Run `java Proxy "http://www.bom.gov.au"`

-   Input `localhost:6331` in a browser to retrieve the modified main page. Enjoy marking!

---

# Required functions

1.  Input url as command line argument: 
    -   Recommend to set `main` method argument in IntelliJ (see above)
    -   I really tried to include external library in command line. It compiles, but when I run the compiled class file, it complains that Jsoup could not be found.
2.  Rewrite html link codes: inside `sendResponse()` method
3.  Modify city codes: `modifyText()`, `replace()` methods
4.  Logs are printed in 4 lines, example:
    >   Sun May 09 20:18:08 CST 2021: GET / HTTP/1.0
    >
    >   Sun May 09 20:18:10 CST 2021: HTTP/1.0 200 OK
    >
    >   Text changes: 41
    >
    >   Link changes: 1

| Capital city | Replaced text |
| ------------ | ------------- |
| Canberra     | CCCC          |
| Sydney       | SSSS          |
| Darwin       | DDDD          |
| Brisbane     | BBBB          |
| Adelaide     | AAAA          |
| Hobart       | HHHH          |
| Melbourne    | MMMM          |
| Perth        | PPPP          |

---

# Technical specifications

-   **Default port**: 6331

-   **Java version**:

    >    openjdk 16 2021-03-16
    >   OpenJDK Runtime Environment (build 16+36-2231)
    >   OpenJDK 64-Bit Server VM (build 16+36-2231, mixed mode, sharing)

-   **URL argument** is accepted only when it is formatted strictly according to RFC2396, checked by `url.toURI()`.

-   **External library** for parsing html: `jsoup-1.13.1`

-   **Proxy server** is constantly running using a `while (true)` loop. (need to terminate by hand)

-   **Proxy client** is written as a method `sendResponse()`, executed when request is accepted.

-   Proxy is tested mainly on **Chrome**, sometimes on **Safari**. Generally, Safari is more stable.

-   I did some garbage collection manually just in case, hoping to improve performance. Those lines are commented by `// gc`. (I do not know C, so I am not sure if I did GC correctly.)

---

# Outcomes

-   **Main page** can be loaded. Texts and links are modified as required, but layout and images could be off. (behaving differently in Chrome and Safari)
-   **Further pages** can be received. Logs are always recorded, but the browser often displays a very incomplete page. Therefore the modified text may not be observed explicitly, but they have been modified according to the logs.
-   **External pages** can be loaded all the time.

---

# Improvements

-   For all String operations, use `StringBuilder` or `StringBuffer` instead. (`modifyText()` and `replace()` methods)