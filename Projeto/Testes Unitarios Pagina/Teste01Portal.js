const puppeteer = require('puppeteer');

test('Clique no card de Licitações redireciona para a página correta', async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto('C:/Users/Carlos/2023-2-Squad10/Projeto/portal.html');

  // Simula o clique no card de Licitações
  await page.click('.card');

  // Aguarda o redirecionamento
  await page.waitForNavigation();

  // Verifica se a URL após o clique é a esperada
  const currentUrl = page.url();
  expect(currentUrl).toBe('C:/Users/Carlos/2023-2-Squad10/Projeto/licitaçao1.html');

  await browser.close();
}, 30000); // Tempo limite de 30 segundos para o teste
