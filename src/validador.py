from pydantic import BaseModel, Field
from datetime import date

class PlanilhaVendas(BaseModel):
    Organizador: int = Field(..., description="ID do organizador responsável pelo anúncio")
    Ano_Mes: str = Field(..., description="Ano e mês do registro no formato YYYY-MM")
    Dia_da_Semana: str = Field(..., description="Dia da semana correspondente à data do anúncio")
    Tipo_Dia: str = Field(..., description="Classificação do dia (ex.: útil, fim de semana, feriado)")
    Objetivo: str = Field(..., description="Objetivo da campanha publicitária")
    Date: date = Field(..., description="Data do anúncio no formato YYYY-MM-DD")
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(..., description="Valor gasto na campanha publicitária")
    Link_clicks: int = Field(..., description="Número de cliques no link do anúncio",nullable=True)
    Impressions: int = Field(..., description="Número de impressões (quantidade de vezes que o anúncio foi exibido)")
    Conversions: int = Field(..., description="Número de conversões realizadas a partir do anúncio")
    Segmentação: str = Field(..., description="Segmentação do público-alvo do anúncio")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio veiculado")
    Fase: str = Field(..., description="Fase da campanha publicitária (ex.: teste, otimização, final)")


