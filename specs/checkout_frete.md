# Especificação do Checkout: Frete

## REQ-01 — Ubiquitous
THE SYSTEM SHALL calcular o valor total adicionando a taxa de
frete padrão de R$ 15,00 ao subtotal do carrinho, exceto quando
a condição de frete grátis de REQ-02 for atendida.

## REQ-02 — IF/THEN
IF o subtotal do carrinho for maior ou igual a R$ 200,00,
THEN THE SYSTEM SHALL conceder frete grátis, com taxa de R$ 0,00.

## Contrato
A entrada é um subtotal numérico, finito e não negativo.

calcular_frete(subtotal) retorna a taxa de frete.
calcular_total(subtotal) retorna o subtotal somado à taxa.

REQ-02 tem prioridade sobre a cobrança padrão de REQ-01.

## Fora do escopo
Cupons, regras por região, banco de dados e interface gráfica.