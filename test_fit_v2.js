const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require("fs");

const html = fs.readFileSync("category.html", "utf-8");

const dom = new JSDOM(html, {
  url: "http://localhost:8080/category.html?cat=fit",
  runScripts: "dangerously",
  resources: "usable"
});

// Since we load the scripts via JSDOM resources (category.html has the script tags),
// we just need to wait for DOMContentLoaded and then wait a bit for fetch to finish.
// Let's mock fetch on the window before scripts run, or intercept it.

dom.window.fetch = async (url) => {
  console.log("Mock fetched:", url);
  if (url.includes("fit")) {
    return {
      ok: true,
      json: async () => [
        { _id: "1", name: "Fit 1", price: 100 },
        { _id: "2", name: "Fit 2", price: 200 },
        { _id: "3", name: "Fit 3", price: 300 }
      ]
    };
  }
  return { ok: true, json: async () => [] };
};

// Polyfill requestAnimationFrame which JSDOM doesn't have
dom.window.requestAnimationFrame = (cb) => setTimeout(cb, 0);

dom.window.addEventListener("load", () => {
  setTimeout(() => {
    console.log("Container innerHTML length:", dom.window.document.getElementById("category-container").innerHTML.length);
    console.log("Container innerHTML snippet:", dom.window.document.getElementById("category-container").innerHTML.substring(0, 500));
    console.log("Errors in DOM:", dom.window.document.getElementById("category-error")?.textContent);
    console.log("Global Errors:", dom.window.document.errors);
  }, 2000);
});
