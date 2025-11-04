import sys
import os


def _import_components():
    """Tenta importar componentes como pacote (relative) e, se falhar,
    tenta importar como módulos de nível superior (execução direta).
    Isso é uma mudança mínima para permitir executar o arquivo tanto
    como módulo de pacote quanto como script direto.
    """
    try:
        
        from .estrategias import PagamentoPix, PagamentoCredito, FreteNormal, FreteExpresso
        from .decoradores import ValorBase, DescontoPix, TaxaEmbalagemPresente
        from .checkout_facade import CheckoutFacade
    except Exception:
        
        from estrategias import PagamentoPix, PagamentoCredito, FreteNormal, FreteExpresso
        from decoradores import ValorBase, DescontoPix, TaxaEmbalagemPresente
        from checkout_facade import CheckoutFacade

    return PagamentoPix, PagamentoCredito, FreteNormal, FreteExpresso, ValorBase, DescontoPix, TaxaEmbalagemPresente, CheckoutFacade


if __name__ == "__main__":
    PagamentoPix, PagamentoCredito, FreteNormal, FreteExpresso, ValorBase, DescontoPix, TaxaEmbalagemPresente, CheckoutFacade = _import_components()

    valor_base = ValorBase(230.0)
    valor_com_desconto = DescontoPix(valor_base)
    checkout = CheckoutFacade(PagamentoPix(), FreteNormal())
    checkout.concluir_transacao(valor_com_desconto)

    print("\n--- Próximo Pedido ---")

    valor_base = ValorBase(600.0)
    valor_com_taxa = TaxaEmbalagemPresente(valor_base)
    checkout = CheckoutFacade(PagamentoCredito(), FreteExpresso())
    checkout.concluir_transacao(valor_com_taxa)