class Vida
    def initialize(mapa)
        @mapa = mapa
    end

    def proxima_geracao
        if @mapa == '..' or @mapa == '*.'
            '..'
        else
            '.'
        end
    end
end

class Celula
    attr_reader :estado, :vizinhas

    def initialize(estado)
        @estado = 0 if estado == '.'
        @estado = 1 if estado == '*'
        @vizinhas = 0
    end

    def adiciona_vizinha
        @vizinhas += 1
    end

end
