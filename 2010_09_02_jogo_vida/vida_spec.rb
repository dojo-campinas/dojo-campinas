require 'vida'

describe Vida, " descrevendo celulas que devem" do
    it "permanecerem mortas se só houver células mortas" do
        vida = Vida.new('.')
        vida.proxima_geracao.should == '.'
        vida = Vida.new('..')
        vida.proxima_geracao.should == '..'
    end
    it "morrer se não tiver pelo menos dois vizinhos vivos" do
        vida = Vida.new('*')
        vida.proxima_geracao.should == '.'
        vida = Vida.new('*.')
        vida.proxima_geracao.should == '..'
    end
end

describe Celula, " descrevendo uma celula" do
    it "tem que saber seu estado atual" do
        cel = Celula.new('.')
        cel.estado.should == 0
        cel = Celula.new('*')
        cel.estado.should == 1
    end

    it "tem que ter 0 vizinhas" do
        cel = Celula.new('.')
        cel.vizinhas.should == 0
    end

    it "tem que poder adicionar vizinhos" do
        cel = Celula.new('.')
        cel.adiciona_vizinha
        cel.vizinhas.should == 1
    end

end
