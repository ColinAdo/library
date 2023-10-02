// Get the PDF URL from the data-pdf-url attribute
    const pdfUrl = document.getElementById("pdf-container").getAttribute("data-pdf-url");

    // Get references to your HTML elements
    const canvas = document.getElementById("pdf-render");
    const prevPageButton = document.getElementById("prev-page");
    const nextPageButton = document.getElementById("next-page");
    const pageNumSpan = document.getElementById("page-num");
    const pageCountSpan = document.getElementById("page-count");

    let pdfDoc = null;
    let pageNum = 1;
    let pageIsRendering = false;
    let pageNumIsPending = null;

    const scale = 1.5;

    // Render the page
    const renderPage = (num) => {
        pageIsRendering = true;

        // Get page
        pdfDoc.getPage(num).then((page) => {
            // Set scale
            const viewport = page.getViewport({ scale });
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            const renderCtx = {
                canvasContext: canvas.getContext("2d"),
                viewport,
            };

            page.render(renderCtx).promise.then(() => {
                pageIsRendering = false;

                if (pageNumIsPending !== null) {
                    renderPage(pageNumIsPending);
                    pageNumIsPending = null;
                }
            });

            // Output current page
            pageNumSpan.textContent = num;
        });
    };

    // Check for pages rendering
    const queueRenderPage = (num) => {
        if (pageIsRendering) {
            pageNumIsPending = num;
        } else {
            renderPage(num);
        }
    };

    // Show Prev Page
    const showPrevPage = () => {
        if (pageNum <= 1) {
            return;
        }
        pageNum--;
        queueRenderPage(pageNum);
    };

    // Show Next Page
    const showNextPage = () => {
        if (pageNum >= pdfDoc.numPages) {
            return;
        }
        pageNum++;
        queueRenderPage(pageNum);
    };

    // Get Document
    pdfjsLib
        .getDocument(pdfUrl) // Use the retrieved PDF URL here
        .promise.then((pdfDoc_) => {
            pdfDoc = pdfDoc_;

            pageCountSpan.textContent = pdfDoc.numPages;

            renderPage(pageNum);
        })
        .catch((err) => {
            // Display error
            const div = document.createElement("div");
            div.className = "error";
            div.appendChild(document.createTextNode(err.message));
            document.querySelector("body").insertBefore(div, canvas);
            // Remove top bar
            document.querySelector(".top-bar").style.display = "none";
        });

    // Button Events
    prevPageButton.addEventListener("click", showPrevPage);
    nextPageButton.addEventListener("click", showNextPage);