const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require("fs");

const html = fs.readFileSync("category.html", "utf-8");
const apiJs = fs.readFileSync("assets/js/api.js", "utf-8");
const categoryJs = fs.readFileSync("assets/js/category.js", "utf-8");

const dom = new JSDOM(html, {
  url: "http://localhost:8080/category.html?cat=fit",
  runScripts: "dangerously",
  resources: "usable"
});

// Since api.js uses fetch, we need to mock it
dom.window.fetch = async (url) => {
  console.log("Fetching:", url);
  if (url.includes("fit")) {
    return {
      json: async () => [
        { _id: "1", name: "Fit 1", price: 100 },
        { _id: "2", name: "Fit 2", price: 200 },
        { _id: "3", name: "Fit 3", price: 300 }
      ]
    };
  }
  return { json: async () => [] };
};

// Inject scripts
const script1 = dom.window.document.createElement("script");
script1.textContent = apiJs;
dom.window.document.body.appendChild(script1);

const script2 = dom.window.document.createElement("script");
script2.textContent = categoryJs;
dom.window.document.body.appendChild(script2);

setTimeout(() => {
  console.log("Container innerHTML:", dom.window.document.getElementById("category-container").innerHTML.substring(0, 500));
  console.log("Errors:", dom.window.document.getElementById("category-error").textContent);
}, 1000);
