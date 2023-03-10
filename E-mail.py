"""
import pandas as pd
import win32com.client as win32

gerentes_df = pd.read_excel('Enviar E-mails.xlsx')
# gerentes_df.info()

for i, email in enumerate(gerentes_df['E-mail']):
    gerente = gerentes_df.loc[i, 'Gerente']
    area = gerentes_df.loc[i, 'Relatório']

    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = 'Relatório de {}'.format(area)
    mail.Body = '''
    Prezado {}, 
    Segue em anexo o Relatório de {}, conforme solicitado.
    Qualquer dúvida estou à disposição.
    Att.,
    '''.format(gerente, area)
    attachment = r'C:\workspace\Integração Python - E-mail\Relatorios{}.xlsx'.format(area)
    mail.Attachments.Add(attachment)

    mail.Send() """