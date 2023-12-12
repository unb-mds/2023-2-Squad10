
  // Descreva seus testes usando Jasmine
  describe('Testes para a página Sobre Projeto', function () {
    // Teste para verificar se o título da página está definido corretamente
    it('Deve ter o título correto', function () {
      expect(document.title).toBe('Sobre Projeto');
    });

    // Teste para verificar se há uma barra de navegação presente
    it('Deve ter uma barra de navegação', function () {
      const navbar = document.querySelector('.navbar');
      expect(navbar).toBeDefined();
    });

    // Adicione mais testes conforme necessário

    // Executar os testes quando a página for carregada
    window.onload = function () {
      jasmine.getEnv().execute();
    };
  });

