import pandas as pd
from datetime import date, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── Configurações ──────────────────────────────────────────
ARQUIVO_EXCEL = "contratos_castanhal_2026.xlsx"
DIAS_AVISO    = 60
EMAIL_ORIGEM  = "aviso202030@gmail.com"
EMAIL_SENHA   = "bsoa gslo rtli unpk"      # senha de app
EMAIL_DESTINO = "luis.henrique0968@gmail.com"
# ──────────────────────────────────────────────────────────

def carregar_contratos():
    df = pd.read_excel(ARQUIVO_EXCEL)
    df.columns = df.columns.str.strip()
    df["Data Vigência"] = pd.to_datetime(df["Data Vigência"])
    return df

def verificar_vencimentos(df):
    hoje    = date.today()
    alertas = []
    for _, row in df.iterrows():
        venc = row["Data Vigência"].date()
        dias = (venc - hoje).days
        if 0 <= dias <= DIAS_AVISO:
            alertas.append({
                "contrato": row["Contrato"],
                "vencimento": venc.strftime("%d/%m/%Y"),
                "dias": dias
            })
    return alertas

def montar_email(alertas):
    linhas = "\n".join(
        f"  • {a['contrato']} — vence em {a['vencimento']} ({a['dias']} dias)"
        for a in alertas
    )
    corpo = f"""Olá,

Os contratos abaixo vencem nos próximos {DIAS_AVISO} dias:

{linhas}

Verifique e tome as providências necessárias.

Atenciosamente,
Sistema de Alertas"""
    return corpo

def enviar_email(corpo):
    msg = MIMEMultipart()
    msg["From"]    = EMAIL_ORIGEM
    msg["To"]      = EMAIL_DESTINO
    msg["Subject"] = f"[ALERTA] Contratos vencendo em {DIAS_AVISO} dias"
    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as srv:
        srv.login(EMAIL_ORIGEM, EMAIL_SENHA)
        srv.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO, msg.as_string())
    print("E-mail enviado com sucesso!")

def main():
    df      = carregar_contratos()
    alertas = verificar_vencimentos(df)
    if alertas:
        print(f"{len(alertas)} contrato(s) próximos do vencimento.")
        corpo = montar_email(alertas)
        enviar_email(corpo)
    else:
        print("Nenhum contrato vence nos próximos 60 dias.")

if __name__ == "__main__":
    main()