// Imprime una guía HTML a PDF A4 con pie de página «Título · Página X de Y».
// uso: node pdf.js entrada.html salida.pdf
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [entrada, salida] = process.argv.slice(2);
  const pie = fs.readFileSync(entrada + '.pie', 'utf8').trim();
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(entrada), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: salida, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;margin:0 19mm;border-top:1px solid #CFD5D9;padding-top:4px;font-family:Carlito,Calibri,sans-serif;font-size:7.5pt;color:#6B7378;display:flex;justify-content:space-between"><span>${pie}</span><span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>`,
  });
  await b.close();
})();
