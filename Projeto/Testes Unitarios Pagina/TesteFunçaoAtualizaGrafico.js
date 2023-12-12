describe('atualizarGrafico', function() {
    let ctx;
    let dados;
  
    beforeEach(function() {
      // Configuração comum para cada teste
      ctx = document.createElement('canvas').getContext('2d');
      dados = [
        { Mes: '1', Ano: '2022', TotalLicitacoes: 10 },
        { Mes: '2', Ano: '2022', TotalLicitacoes: 20 }
        // Adicione mais dados conforme necessário
      ];
    });
  
    it('deve atualizar o gráfico corretamente', function() {
      atualizarGrafico(ctx, dados);
  
      // Adicione asserções para verificar se o gráfico foi criado corretamente
      expect(ctx.canvas).toBeTruthy();
      expect(ctx.canvas.id).toEqual('myChart');
      // Adicione mais asserções conforme necessário
    });
  
    // Adicione mais testes conforme necessário
  });
  