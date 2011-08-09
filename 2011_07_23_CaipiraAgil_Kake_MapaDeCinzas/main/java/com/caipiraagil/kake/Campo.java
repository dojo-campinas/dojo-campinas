package com.caipiraagil.kake;

/**
 * @author jonasabreu
 * 
 */
final public class Campo {

	private String[][] campo;

	public Campo(final int altura, final int largura) {
		campo = new String[altura][largura];
		for (String[] linha : campo) {
			for (int i = 0; i < linha.length; i++) {
				linha[i] = ".";
			}
		}
	}

	public String posicao(final int linha, final int coluna) {
		return campo[linha][coluna];
	}

	public void insereAeroporto(final int linha, final int coluna) {
		campo[linha][coluna] = "A";
	}

	public void insereNuvem(final int linha, final int coluna) {
		campo[linha][coluna] = "*";
	}

	public void passaDia() {
		Campo novoCampo = new Campo(campo.length, campo[0].length);

		for (int i = 0; i < campo.length; i++) {
			for (int j = 0; j < campo[i].length; j++) {
				novoCampo.campo[i][j] = campo[i][j];
				if (posicao(i, j).equals("*")) {
					if (i + 1 < campo.length) {
						novoCampo.insereNuvem(i + 1, j);
					}
					if (j + 1 < campo[i].length) {
						novoCampo.insereNuvem(i, j + 1);
					}
				}
			}
		}

		campo = novoCampo.campo;
	}
}
