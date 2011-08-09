package com.caipiraagil.kake;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

/**
 * @author jonasabreu
 * 
 */
final public class CampoTest {

	private Campo campo;

	@Before
	public void setup() {
		campo = new Campo(2, 2);
	}

	@Test
	public void testaQueCampoIniciaVazio() {
		assertEquals(".", campo.posicao(0, 0));
		assertEquals(".", campo.posicao(1, 0));
	}

	@Test
	public void testaQueMarcaPosicaoDeAeroporto() {
		campo.insereAeroporto(1, 0);
		assertEquals("A", campo.posicao(1, 0));
	}

	@Test
	public void testaQueMarcaPosicaoDeNuvem() {
		campo.insereNuvem(1, 0);
		assertEquals("*", campo.posicao(1, 0));
	}

	@Test
	public void testaPosicao() {
		assertEquals(".", campo.posicao(0, 0));
		campo.insereNuvem(0, 0);
		assertEquals("*", campo.posicao(0, 0));
		campo.insereAeroporto(0, 0);
		assertEquals("A", campo.posicao(0, 0));
	}

	@Test
	public void testaPassaDiaComNuvem() {
		campo.insereNuvem(0, 0);
		campo.passaDia();
		assertEquals("*", campo.posicao(0, 0));
		assertEquals("*", campo.posicao(1, 0));
	}

	@Test
	public void testaPassaDiaComNuvemTrocada() {
		campo.insereNuvem(1, 0);
		campo.passaDia();
		assertEquals("*", campo.posicao(0, 0));
		assertEquals("*", campo.posicao(1, 0));
	}

	@Test
	public void testaPassaDiaSemNuvem() {
		campo.passaDia();
		assertEquals(".", campo.posicao(0, 0));
		assertEquals(".", campo.posicao(1, 0));
	}

	@Test
	public void testaPassaDiaComNuvemNoCampo2x2() {
		campo.insereNuvem(0, 0);
		campo.passaDia();
		assertEquals("*", campo.posicao(0, 0));
		assertEquals("*", campo.posicao(1, 0));
		assertEquals("*", campo.posicao(0, 1));
		assertEquals(".", campo.posicao(1, 1));
	}

}
