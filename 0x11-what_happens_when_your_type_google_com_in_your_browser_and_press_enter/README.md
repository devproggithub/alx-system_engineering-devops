What happens when you type google.com in your browser

------------------------------------------------------
Based on the information I found, when the “g” key is pressed in the browser, the following happens:

The browser receives the event and the auto-complete functions kick in.
Depending on your browser’s algorithm and if you are in private/incognito mode or not, various suggestions will be presented to you in the dropdown below the URL bar.
Most of these algorithms sort and prioritize results based on search history, bookmarks, cookies, and popular searches from the internet as a whole.
As you are typing “google.com”, many blocks of code run and the suggestions will be refined with each key press.
It may even suggest “google.com” before you finish typing it.
----------------------------------------------------------
Q: What happens when you type google.com in your browser?

Upon typing in "google.com" and pressing Enter, the browser takes a number of steps which can be outlined as:

Resolve IP address of the URL via DNS
Generate an HTTP request with headers (accept, user-agent, cookie, etc)
Open an HTTP connection to the resolved IP address
Send the request to the server
Receive the response from the server
Parse response headers
Depending on the response headers, perform additional operations
Decompress the response body if it's compressed (e.g. gzipped)
Parse the HTML code inside the response body
Resolve any additional resources (images, stylesheets, scripts, etc)
Start loading those resources via their URLs using the same steps
Render the HTML as soon as required resources are loaded, continue loading remaining resources in background
When all the resources are loaded, close the HTTP connection
Q: What are "additional operations" that a browser can perform depending on response headers?

For example, it can redirect to a different resource on a 301/302/303/307 status code and a location header.

Browsers also respect policies regulated by the server, e.g. cache-control header which instructs how the resources can be cached.

Response headers may also contain information regarding the response content, including its type, length, and encoding, which may be used by the browser to properly display the content.
