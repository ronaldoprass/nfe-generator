import random
import argparse
import os
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom

def calcular_dv(chave):
    """Calcula o dígito verificador da chave de acesso"""
    pesos = [4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2] * 4
    soma = sum(int(chave[i]) * pesos[i] for i in range(43))
    resto = soma % 11
    dv = 0 if resto < 2 else 11 - resto
    return str(dv)

def gerar_chave():
    """Gera uma chave de acesso de exemplo"""
    cUF = '35'  # Código da UF
    AAMM = '2407'  # Ano e mês de emissão
    CNPJ = '12345678000199'  # CNPJ do emitente
    mod = '55'  # Modelo da NFe
    serie = '001'  # Série da NFe
    nNF = str(random.randint(1, 99999999)).zfill(9)  # Número da NFe
    tpEmis = '1'  # Forma de emissão
    cNF = str(random.randint(0, 99999999)).zfill(8)  # Código numérico
    chave = f'{cUF}{AAMM}{CNPJ}{mod}{serie}{nNF}{tpEmis}{cNF}'
    chave += calcular_dv(chave)  # Adiciona o dígito verificador
    return chave

def gerar_chaves(quantidade):
    """Gera uma lista de chaves de acesso"""
    return [gerar_chave() for _ in range(quantidade)]

def salvar_chaves(chaves, diretorio):
    """Salva as chaves geradas em um arquivo de texto"""
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    with open(os.path.join(diretorio, 'chaves_nfe.txt'), 'w') as f:
        for chave in chaves:
            f.write(f"{chave}\n")

def criar_arquivo_xml(chave, diretorio):
    """Cria um arquivo XML de exemplo com base na chave de acesso"""
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    nfe = Element('NFe', xmlns="http://www.portalfiscal.inf.br/nfe")
    infNFe = SubElement(nfe, 'infNFe', Id=f'NFe{chave}', versao="4.00")
    
    ide = SubElement(infNFe, 'ide')
    SubElement(ide, 'cUF').text = '35'
    SubElement(ide, 'cNF').text = chave[35:43]
    SubElement(ide, 'natOp').text = 'Venda de mercadorias'
    SubElement(ide, 'mod').text = '55'
    SubElement(ide, 'serie').text = '1'
    SubElement(ide, 'nNF').text = '1'
    SubElement(ide, 'dhEmi').text = '2024-07-08T08:00:00-03:00'
    SubElement(ide, 'tpNF').text = '1'
    SubElement(ide, 'idDest').text = '1'
    SubElement(ide, 'cMunFG').text = '3550308'
    SubElement(ide, 'tpImp').text = '1'
    SubElement(ide, 'tpEmis').text = '1'
    SubElement(ide, 'cDV').text = chave[-1]
    SubElement(ide, 'tpAmb').text = '2'
    SubElement(ide, 'finNFe').text = '1'
    SubElement(ide, 'indFinal').text = '1'
    SubElement(ide, 'indPres').text = '1'
    SubElement(ide, 'procEmi').text = '0'
    SubElement(ide, 'verProc').text = '4.00'
    
    emit = SubElement(infNFe, 'emit')
    SubElement(emit, 'CNPJ').text = '12345678000199'
    SubElement(emit, 'xNome').text = 'Emitente Fictício Ltda'
    enderEmit = SubElement(emit, 'enderEmit')
    SubElement(enderEmit, 'xLgr').text = 'Rua Exemplo'
    SubElement(enderEmit, 'nro').text = '123'
    SubElement(enderEmit, 'xBairro').text = 'Centro'
    SubElement(enderEmit, 'cMun').text = '3550308'
    SubElement(enderEmit, 'xMun').text = 'São Paulo'
    SubElement(enderEmit, 'UF').text = 'SP'
    SubElement(enderEmit, 'CEP').text = '01000000'
    SubElement(enderEmit, 'cPais').text = '1058'
    SubElement(enderEmit, 'xPais').text = 'Brasil'
    SubElement(enderEmit, 'fone').text = '1133334444'
    SubElement(emit, 'IE').text = '123456789'
    SubElement(emit, 'CRT').text = '3'
    
    dest = SubElement(infNFe, 'dest')
    SubElement(dest, 'CNPJ').text = '98765432000188'
    SubElement(dest, 'xNome').text = 'Destinatário Fictício S/A'
    enderDest = SubElement(dest, 'enderDest')
    SubElement(enderDest, 'xLgr').text = 'Avenida Exemplo'
    SubElement(enderDest, 'nro').text = '456'
    SubElement(enderDest, 'xBairro').text = 'Centro'
    SubElement(enderDest, 'cMun').text = '3550308'
    SubElement(enderDest, 'xMun').text = 'São Paulo'
    SubElement(enderDest, 'UF').text = 'SP'
    SubElement(enderDest, 'CEP').text = '01000000'
    SubElement(enderDest, 'cPais').text = '1058'
    SubElement(enderDest, 'xPais').text = 'Brasil'
    SubElement(enderDest, 'fone').text = '1199998888'
    SubElement(dest, 'indIEDest').text = '1'
    SubElement(dest, 'IE').text = '987654321'
    SubElement(dest, 'email').text = 'destinatario@exemplo.com'
    
    det = SubElement(infNFe, 'det', nItem="1")
    prod = SubElement(det, 'prod')
    SubElement(prod, 'cProd').text = '12345'
    SubElement(prod, 'cEAN').text = 'SEM GTIN'
    SubElement(prod, 'xProd').text = 'Produto Exemplo'
    SubElement(prod, 'NCM').text = '61091000'
    SubElement(prod, 'CFOP').text = '5102'
    SubElement(prod, 'uCom').text = 'UN'
    SubElement(prod, 'qCom').text = '10.0000'
    SubElement(prod, 'vUnCom').text = '10.00'
    SubElement(prod, 'vProd').text = '100.00'
    SubElement(prod, 'cEANTrib').text = 'SEM GTIN'
    SubElement(prod, 'uTrib').text = 'UN'
    SubElement(prod, 'qTrib').text = '10.0000'
    SubElement(prod, 'vUnTrib').text = '10.00'
    SubElement(prod, 'indTot').text = '1'
    
    imposto = SubElement(det, 'imposto')
    icms = SubElement(imposto, 'ICMS')
    icms00 = SubElement(icms, 'ICMS00')
    SubElement(icms00, 'orig').text = '0'
    SubElement(icms00, 'CST').text = '00'
    SubElement(icms00, 'modBC').text = '3'
    SubElement(icms00, 'vBC').text = '100.00'
    SubElement(icms00, 'pICMS').text = '18.00'
    SubElement(icms00, 'vICMS').text = '18.00'
    
    total = SubElement(infNFe, 'total')
    icmstot = SubElement(total, 'ICMSTot')
    SubElement(icmstot, 'vBC').text = '100.00'
    SubElement(icmstot, 'vICMS').text = '18.00'
    SubElement(icmstot, 'vICMSDeson').text = '0.00'
    SubElement(icmstot, 'vFCPUFDest').text = '0.00'
    SubElement(icmstot, 'vICMSUFDest').text = '0.00'
    SubElement(icmstot, 'vICMSUFRemet').text = '0.00'
    SubElement(icmstot, 'vFCP').text = '0.00'
    SubElement(icmstot, 'vBCST').text = '0.00'
    SubElement(icmstot, 'vST').text = '0.00'
    SubElement(icmstot, 'vFCPST').text = '0.00'
    SubElement(icmstot, 'vFCPSTRet').text = '0.00'
    SubElement(icmstot, 'vProd').text = '100.00'
    SubElement(icmstot, 'vFrete').text = '0.00'
    SubElement(icmstot, 'vSeg').text = '0.00'
    SubElement(icmstot, 'vDesc').text = '0.00'
    SubElement(icmstot, 'vII').text = '0.00'
    SubElement(icmstot, 'vIPI').text = '0.00'
    SubElement(icmstot, 'vIPIDevol').text = '0.00'
    SubElement(icmstot, 'vPIS').text = '0.00'
    SubElement(icmstot, 'vCOFINS').text = '0.00'
    SubElement(icmstot, 'vOutro').text = '0.00'
    SubElement(icmstot, 'vNF').text = '100.00'
    
    transp = SubElement(infNFe, 'transp')
    SubElement(transp, 'modFrete').text = '0'
    
    pag = SubElement(infNFe, 'pag')
    detPag = SubElement(pag, 'detPag')
    SubElement(detPag, 'tPag').text = '01'
    SubElement(detPag, 'vPag').text = '100.00'
    
    infNFeSupl = SubElement(nfe, 'infNFeSupl')
    SubElement(infNFeSupl, 'qrCode').text = f'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p={chave}|2|1|1|18.00|100.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00'
    SubElement(infNFeSupl, 'urlChave').text = f'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p={chave}'
    
    xml_str = xml.dom.minidom.parseString(tostring(nfe)).toprettyxml(indent="  ")
    with open(os.path.join(diretorio, f"NFe{chave}.xml"), "w") as f:
        f.write(xml_str)

# Configuração do argparse
parser = argparse.ArgumentParser(description='Gerar chaves de NF-e e arquivos XML correspondentes.')
parser.add_argument('quantidade', type=int, help='Quantidade de chaves de acesso a serem geradas')

args = parser.parse_args()

# Gera a quantidade de chaves especificada pelo usuário
chaves = gerar_chaves(args.quantidade)

# Salva as chaves em um arquivo de texto na pasta chaves
salvar_chaves(chaves, 'chaves')

# Cria arquivos XML na pasta nfe para cada chave gerada
for chave in chaves:
    criar_arquivo_xml(chave, 'nfe')

