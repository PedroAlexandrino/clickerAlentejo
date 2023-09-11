from django.shortcuts import render
from .models import *
import os

from xlwt import Workbook
from datetime import datetime,timedelta
from django.http import JsonResponse, FileResponse
from django.shortcuts import render, redirect


#                 -------------------------FUNCS  DA PAGINA DOS CLICKS-------------------------
def nova_pagina(request):
    from datetime import datetime, time
    print("teste")
    agora = datetime.now()
    timestamp = agora.strftime('%d/%m/%Y')
    p1_inicio = datetime.strptime(P1.objects.values("p1_inicio").first()["p1_inicio"], '%H:%M').time()
    p1_fim = datetime.strptime(P1.objects.values("p1_fim").first()["p1_fim"], '%H:%M').time()

    p2_inicio = datetime.strptime(P2.objects.values("p2_inicio").first()["p2_inicio"], '%H:%M').time()
    p2_fim = datetime.strptime(P2.objects.values("p2_fim").first()["p2_fim"], '%H:%M').time()

    p3_inicio = datetime.strptime(P3.objects.values("p3_inicio").first()["p3_inicio"], '%H:%M').time()
    p3_fim = datetime.strptime(P3.objects.values("p3_fim").first()["p3_fim"], '%H:%M').time()
    periodo = ""
    if p1_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p1_fim.strftime("%H:%M"):
        periodoAtual = "P1"
        print("p1")
        periodo = "Primeiro Turno"
        contador_atual = len(Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p1_inicio.strftime("%H:%M")}' AND '{timestamp} {p1_fim.strftime("%H:%M")}'"""))
    
    elif p2_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p2_fim.strftime("%H:%M"):
        print("P2")
        periodo = "Segundo Turno"
        periodoAtual = "P2"
        contador_atual = len(Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p2_inicio.strftime("%H:%M")}' AND '{timestamp} {p2_fim.strftime("%H:%M")}'"""))
    
    elif p3_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p3_fim.strftime("%H:%M"):
        print("P3")
        periodoAtual = "P3"
        periodo = "Terceiro Turno"
        contador_atual = len(Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p3_inicio.strftime("%H:%M")}' AND '{timestamp} {p3_fim.strftime("%H:%M")}'"""))
    else:
        print("Fora dos períodos definidos")
        periodo = "Ainda não está nenhum periodo ativo"
        periodoAtual = "Fora dos períodos definidos"
        contador_atual = len(Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view"""))

    #contador para ver quantos cliques já foram feitos hoje
    print("P2",p1_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p1_fim.strftime("%H:%M"),p1_inicio.strftime("%H:%M") , agora.strftime("%H:%M") , p1_fim.strftime("%H:%M"))
    print("p1_inicio",Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p1_inicio.strftime("%H:%M")}' AND '{timestamp} {p1_fim.strftime("%H:%M")}'"""))
    print("p2_inicio",Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p2_inicio.strftime("%H:%M")}' AND '{timestamp} {p2_fim.strftime("%H:%M")}'"""))
    print("p3_inicio",Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p3_inicio.strftime("%H:%M")}' AND '{timestamp} {p3_fim.strftime("%H:%M")}'"""))

    contador_atualp1 = len(Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p1_inicio.strftime("%H:%M")}' AND '{timestamp} {p1_fim.strftime("%H:%M")}'"""))
    contador_atualp2 = len(Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p2_inicio.strftime("%H:%M")}' AND '{timestamp} {p2_fim.strftime("%H:%M")}'"""))
    contador_atualp3 = len(Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p3_inicio.strftime("%H:%M")}' AND '{timestamp} {p3_fim.strftime("%H:%M")}'"""))
    
    print("vai abrir nova pagina",periodo)
    #return render(request, 'nova_pagina.html')
    return render(request, "nova_pagina.html", {
            "periodo": periodo,
            "contador_atual":contador_atual,
            "contador_atualp1": contador_atualp1,
            "contador_atualp2": contador_atualp2,
            "contador_atualp3": contador_atualp3})


def addContador(request=None):
    print("nReps->",request.POST["nReps"])
    if request.POST["nReps"] != "1":
        for x in range(1,int(request.POST["nReps"])+1):
            agora = datetime.now()
            p1_inicio = datetime.strptime(P1.objects.values("p1_inicio").first()["p1_inicio"], '%H:%M').time()
            p1_fim = datetime.strptime(P1.objects.values("p1_fim").first()["p1_fim"], '%H:%M').time()

            p2_inicio = datetime.strptime(P2.objects.values("p2_inicio").first()["p2_inicio"], '%H:%M').time()
            p2_fim = datetime.strptime(P2.objects.values("p2_fim").first()["p2_fim"], '%H:%M').time()

            p3_inicio = datetime.strptime(P3.objects.values("p3_inicio").first()["p3_inicio"], '%H:%M').time()
            p3_fim = datetime.strptime(P3.objects.values("p3_fim").first()["p3_fim"], '%H:%M').time()
            turno = ""
            if p1_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p1_fim.strftime("%H:%M"):
                turno = "T1"
                print("p1")
            
            elif p2_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p2_fim.strftime("%H:%M"):
                print("P2")
                turno = "T2"
            
            elif p3_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p3_fim.strftime("%H:%M"):
                print("P3")
                turno = "T3"
                    
            print("vai adicionar uma linha à bd do contador com 1 / data")
            agora = datetime.now()
            timestamp = agora.strftime('%d/%m/%Y %H:%M')
            print("time->",timestamp)
            Contador(contador = "1",data = timestamp, turno = turno).save()
        return JsonResponse("OK",safe=False)
    else:
        
        agora = datetime.now()
        p1_inicio = datetime.strptime(P1.objects.values("p1_inicio").first()["p1_inicio"], '%H:%M').time()
        p1_fim = datetime.strptime(P1.objects.values("p1_fim").first()["p1_fim"], '%H:%M').time()

        p2_inicio = datetime.strptime(P2.objects.values("p2_inicio").first()["p2_inicio"], '%H:%M').time()
        p2_fim = datetime.strptime(P2.objects.values("p2_fim").first()["p2_fim"], '%H:%M').time()

        p3_inicio = datetime.strptime(P3.objects.values("p3_inicio").first()["p3_inicio"], '%H:%M').time()
        p3_fim = datetime.strptime(P3.objects.values("p3_fim").first()["p3_fim"], '%H:%M').time()
        turno = ""
        if p1_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p1_fim.strftime("%H:%M"):
            turno = "T1"
            print("p1")
        
        elif p2_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p2_fim.strftime("%H:%M"):
            print("P2")
            turno = "T2"
        
        elif p3_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p3_fim.strftime("%H:%M"):
            print("P3")
            turno = "T3"
                
        print("vai adicionar uma linha à bd do contador com 1 / data")
        agora = datetime.now()
        timestamp = agora.strftime('%d/%m/%Y %H:%M')
        print("time->",timestamp)
        Contador(contador = "1",data = timestamp, turno = turno).save()
        return JsonResponse("OK",safe=False)


def getCliques(request=None):
    print("Entrou no getCliques")
    if request.POST["start_date"]:
        """
        TENS DE CRIAR UM ARRAY COM OS DIAS QUE ESTÃO ENTRE O START_DATE E O END_DATE, PRECORRER COM UM FOR E IR SOMANDO Á VARIAVEL QUE
        VAI GUARDAR O TOTAL DE CADA TURNO PARA OS DIAS QUE FORAM SELECIONADOS.
        O PROBLEMA É QUE ESTA FUNC getCliques() ESTÁ A TRABALHAR COM OS DADOS ATUAIS DOS TURNOS, OU SEJA
        SE HOUVE UMA FEIRA EM QUE O PRIMEIRO TURNO COMEÇOU ÀS 10 E ACABOU ÀS 14 PODE NÃO SE REFLETIR NA FEIRA ATUAL E ESSES CLIQUES QUE FICAM
        DE FORA POR CAUSA DOS TURNOS DA FEIRA ATUAL, NÃO SAÃO CONTABILIZADOS.
        """
        d2 = datetime.strptime(request.POST["end_date"], '%d/%m/%Y')
        d1 = datetime.strptime(request.POST["start_date"], '%d/%m/%Y')
        dias = []
        quantidade_dias = d1

        contador_p1 =0
        contador_p2 =0
        contador_p3 =0

        while quantidade_dias <= d2:
            dias.append(quantidade_dias.strftime('%d/%m/%Y'))
            
            print(quantidade_dias.strftime('%d/%m/%Y'),type(quantidade_dias.strftime('%d/%m/%Y')))
            print(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T1'"""))


            contador_p1 += len(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T1'"""))
            
            contador_p2 +=  len(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T2'"""))

            contador_p3 += len(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T3'"""))

            quantidade_dias += timedelta(days=1)

        return JsonResponse({"contador_atualp1": contador_p1,"contador_atualp2": contador_p2,"contador_atualp3": contador_p3})   

    else:    
        print("entrou no else, getCliques")
        agora = datetime.now()
        timestamp = agora.strftime('%d/%m/%Y')
        p1_inicio = datetime.strptime(P1.objects.values("p1_inicio").first()["p1_inicio"], '%H:%M').time()
        p1_fim = datetime.strptime(P1.objects.values("p1_fim").first()["p1_fim"], '%H:%M').time()

        p2_inicio = datetime.strptime(P2.objects.values("p2_inicio").first()["p2_inicio"], '%H:%M').time()
        p2_fim = datetime.strptime(P2.objects.values("p2_fim").first()["p2_fim"], '%H:%M').time()

        p3_inicio = datetime.strptime(P3.objects.values("p3_inicio").first()["p3_inicio"], '%H:%M').time()
        p3_fim = datetime.strptime(P3.objects.values("p3_fim").first()["p3_fim"], '%H:%M').time()

        print("p1 getCliques",timestamp)
        contador_atualp1 = len(Contador.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p1_inicio.strftime("%H:%M")}' AND '{timestamp} {p1_fim.strftime("%H:%M")}'"""))
        print("P2 getCliques")
        contador_atualp2 = len(Contador.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p2_inicio.strftime("%H:%M")}' AND '{timestamp} {p2_fim.strftime("%H:%M")}'"""))
        print("P3 getCliques")
        contador_atualp3 = len(Contador.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p3_inicio.strftime("%H:%M")}' AND '{timestamp} {p3_fim.strftime("%H:%M")}'"""))
        
        contador_atualTOTAL = len(Contador.objects.raw(f"""SELECT * FROM clicker_contador"""))
        print("P2",datetime.combine(datetime.now().date(), p1_inicio),p2_inicio.strftime("%H:%M"))
        print("p1_inicio",Contador.objects.raw(f"""SELECT * FROM clicker_contador WHERE data BETWEEN '{timestamp} {p1_inicio.strftime("%H:%M")}' AND '{timestamp} {p1_fim.strftime("%H:%M")}'"""))
        print("p2_inicio",Contador.objects.raw(f"""SELECT * FROM clicker_contador WHERE data BETWEEN '{timestamp} {p2_inicio.strftime("%H:%M")}' AND '{timestamp} {p2_fim.strftime("%H:%M")}'"""))
        print("p3_inicio",Contador.objects.raw(f"""SELECT * FROM clicker_contador WHERE data BETWEEN '{timestamp} {p3_inicio.strftime("%H:%M")}' AND '{timestamp} {p3_fim.strftime("%H:%M")}'"""))

    return JsonResponse({"contador_atualp1": contador_atualp1,"contador_atualp2": contador_atualp2,"contador_atualp3": contador_atualp3})


def getPerguntas(request=None):
    print("Vai pegar as perguntas e devolver em json")
    #perguntas = Pergunta.objects.all()
    perguntas = Pergunta.objects.all()
    print("perguntas",perguntas)
    perguntasFinal=[item.to_dict() for item in perguntas]

    return JsonResponse(perguntasFinal,safe=False)


def elimina_ultimo_valor(request=None):
    print("vai eliminar ultimo valor da bd")
    Contador.objects.last().delete()
    return JsonResponse("OK",safe=False)

def add_pergunta(request=None):
    print("vai adicionar pergunta",request.POST)
    agora = datetime.now()
    timestamp = agora.strftime('%d/%m/%Y %H:%M')
    Pergunta(pergunta=request.POST["pergunta"],data=timestamp).save()

    return JsonResponse({"response": "ok"})



def download_excel_all_final_dia(request):
    print("REQUEST SE TIVER DATAS->",request.POST)
    elementos = Contador.objects
    import io   

    agora = datetime.now()
    timestamp = agora.strftime('%d/%m/%Y')
    p1_inicio = datetime.strptime(P1.objects.values("p1_inicio").first()["p1_inicio"], '%H:%M').time()
    p1_fim = datetime.strptime(P1.objects.values("p1_fim").first()["p1_fim"], '%H:%M').time()
    
    p2_inicio = datetime.strptime(P2.objects.values("p2_inicio").first()["p2_inicio"], '%H:%M').time()
    p2_fim = datetime.strptime(P2.objects.values("p2_fim").first()["p2_fim"], '%H:%M').time()

    p3_inicio = datetime.strptime(P3.objects.values("p3_inicio").first()["p3_inicio"], '%H:%M').time()
    p3_fim = datetime.strptime(P3.objects.values("p3_fim").first()["p3_fim"], '%H:%M').time()

    if request.POST["start_date"]:
        d2 = datetime.strptime(request.POST["end_date"], '%d/%m/%Y')
        d1 = datetime.strptime(request.POST["start_date"], '%d/%m/%Y')
        dias = []
        quantidade_dias = d1

        contador_p1 =0
        contador_p2 =0
        contador_p3 =0

        while quantidade_dias <= d2:
            dias.append(quantidade_dias.strftime('%d/%m/%Y'))
            
            print(quantidade_dias.strftime('%d/%m/%Y'),type(quantidade_dias.strftime('%d/%m/%Y')))
            print(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T1'"""))


            contador_p1 += len(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T1'"""))
            
            contador_p2 +=  len(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T2'"""))

            contador_p3 += len(Contador.objects.raw(f"""SELECT clicker_contador.id,"contador","data" FROM clicker_contador 
            WHERE data LIKE '{quantidade_dias.strftime('%d/%m/%Y')}%%' AND turno = 'T3'"""))
            quantidade_dias += timedelta(days=1)

        caminho = 'C:/visteon/media/shippers/portaria'
        if os.path.exists(caminho):
            for entry in os.listdir(caminho):
                if os.path.isfile(os.path.join(caminho, entry)):
                    os.remove(caminho + "/" + entry)

        wbProduction = Workbook()
        sheetProduction = wbProduction.add_sheet("Sheet 1")

        row = 0
        col = 0
        #titulos
        sheetProduction.write(row, col, "TURNO 1")
        sheetProduction.write(row, col + 1, "TURNO 2")
        sheetProduction.write(row, col + 2, "TURNO 3")
        sheetProduction.write(row, col + 3, "TOTAL:")
        row += 1
        sheetProduction.write(row, col, contador_p1)
        sheetProduction.write(row, col + 1, contador_p2)
        sheetProduction.write(row, col + 2, contador_p3)    
        sheetProduction.write(row, col + 3, contador_p1 + contador_p2 + contador_p3)
    else:
        p1 = Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p1_inicio.strftime("%H:%M")}' AND '{timestamp} {p1_fim.strftime("%H:%M")}'""")
        p2 = Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p2_inicio.strftime("%H:%M")}' AND '{timestamp} {p2_fim.strftime("%H:%M")}'""")
        p3 = Contador_View.objects.raw(f"""SELECT * FROM clicker_contador_view WHERE data BETWEEN '{timestamp} {p3_inicio.strftime("%H:%M")}' AND '{timestamp} {p3_fim.strftime("%H:%M")}'""")

    #para testar/alterar

        caminho = 'C:/visteon/media/shippers/portaria'
        if os.path.exists(caminho):
            for entry in os.listdir(caminho):
                if os.path.isfile(os.path.join(caminho, entry)):
                    os.remove(caminho + "/" + entry)

        wbProduction = Workbook()
        sheetProduction = wbProduction.add_sheet("Sheet 1")

        row = 0
        col = 0
        #titulos
        sheetProduction.write(row, col, "TURNO 1")
        sheetProduction.write(row, col + 1, "TURNO 2")
        sheetProduction.write(row, col + 2, "TURNO 3")
        sheetProduction.write(row, col + 3, "TOTAL:")
        row += 1
        sheetProduction.write(row, col, len(p1))
        sheetProduction.write(row, col + 1, len(p2))
        sheetProduction.write(row, col + 2, len(p3))    
        sheetProduction.write(row, col + 3, len(p1) + len(p2) + len(p3))
    row += 1
    row += 2
    sheetProduction.write(row, col, "PERGUNTAS:")

    for i in Pergunta.objects.all():
        row += 1

        sheetProduction.write(row, col,i.pergunta)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Concatena o diretório base com o diretório desejado dentro do projeto
    diretorio_destino = os.path.join(base_dir, 'clickerAlentejo', 'ficheiros')

    # Verifica se o diretório de destino existe, caso contrário, crie-o
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Define o caminho completo para o arquivo Excel
    caminho_arquivo = os.path.join(diretorio_destino, 'excel_clickers_diario.xls')

    # Salva o arquivo Excel no caminho especificado
    wbProduction.save(caminho_arquivo)
    print("caminho_arquivo",caminho_arquivo)
    #wbProduction.save("C:\\visteon\\media\\shippers\\portaria\\workbookPortaria.xls")
    file = io.BytesIO()
    wbProduction.save(file)
    file.seek(0) 
    #return redirect('clicker:nova_pagina')
    fresp = FileResponse(
            file, filename=f"excel_clickers_diario{agora.strftime('%d:%m:%Y')}.xls", as_attachment=True
        )
    return fresp
    return redirect("/")



#                 -------------------------FIM CLICKS-------------------------




#                 -------------------------FUNCS  DA PAGINA DOS PERIODOS-------------------------
def configurations(request):
    from datetime import datetime, time
    print("teste")
    agora = datetime.now()
    timestamp = agora.strftime('%d/%m/%Y')
    p1_inicio = datetime.strptime(P1.objects.values("p1_inicio").first()["p1_inicio"], '%H:%M').time()
    p1_fim = datetime.strptime(P1.objects.values("p1_fim").first()["p1_fim"], '%H:%M').time()

    p2_inicio = datetime.strptime(P2.objects.values("p2_inicio").first()["p2_inicio"], '%H:%M').time()
    p2_fim = datetime.strptime(P2.objects.values("p2_fim").first()["p2_fim"], '%H:%M').time()

    p3_inicio = datetime.strptime(P3.objects.values("p3_inicio").first()["p3_inicio"], '%H:%M').time()
    p3_fim = datetime.strptime(P3.objects.values("p3_fim").first()["p3_fim"], '%H:%M').time()
    periodo = ""
    if p1_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p1_fim.strftime("%H:%M"):
        periodoAtual = "P1"
        print("p1")
        periodo = "Primeiro Turno"
    elif p2_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p2_fim.strftime("%H:%M"):
        print("P2")
        periodo = "Segundo Turno"
    elif p3_inicio.strftime("%H:%M") <= agora.strftime("%H:%M") <= p3_fim.strftime("%H:%M"):
        print("P3")
        periodo = "Terceiro Turno"
    else:
        print("Fora dos períodos definidos")
        periodo = "Ainda não está nenhum periodo ativo"
    
    
    print("p1_inicio",p1_inicio)

    return render(request, "configurations.html", {
            "p1_inicio" : p1_inicio,
            "p1_fim" : p1_fim,
            "p2_inicio" : p2_inicio,
            "p2_fim" : p2_fim,
            "p3_inicio" : p3_inicio,
            "p3_fim" : p3_fim,
            "periodo": periodo})


def add_periodo(request=None):
    print("req->", request.POST)

    periodo = request.POST["periodo"]
    inputValue = replace_symbol(request.POST["inputValue"])

    if periodo == "p1_inicio":
        P1.objects.update_or_create(defaults={'p1_inicio': inputValue})

    elif periodo == "p1_fim":
        P1.objects.update_or_create(defaults={'p1_fim': inputValue})

    elif periodo == "p2_inicio":
        P2.objects.update_or_create(defaults={'p2_inicio': inputValue})

    elif periodo == "p2_fim":
        P2.objects.update_or_create(defaults={'p2_fim': inputValue})

    elif periodo == "p3_inicio":
        P3.objects.update_or_create(defaults={'p3_inicio': inputValue})

    else:
        P3.objects.update_or_create(defaults={'p3_fim': inputValue})
    return render(request, 'configurations.html')

def replace_symbol(input_string):
    symbols = [",", ".", "-"]  # Símbolos a serem substituídos por ":"
    for symbol in symbols:
        input_string = input_string.replace(symbol, ":")

    return input_string

#                 -------------------------FIM FUNCS PERIODOS-------------------------




#                 -------------------------FUNCS PAGINA DO REGISTO DE COMPRAS-------------------------

def home_registo_compras(request):
    #fechar_contas()
    print("teste")
    compras = Compras_View.objects.all()
    pessoas = Compras_View.objects.raw("""SELECT MIN(id) AS id, "nPessoa" FROM clicker_compras GROUP BY "nPessoa" """)
    pessoas_list = [item.nPessoa for item in pessoas]
    fechar_contas1()
    

    return render(request, "registoCompras.html", {
        "compras": compras,
        "pessoas_list":pessoas_list})
    return render(request, 'registoCompras.html')

def add_compra(request):
    agora = datetime.now()
    timestamp = agora.strftime('%d/%m/%Y %H:%M')
    print("Vai adicionar compra",timestamp)

    Compras(
        nPessoa = request.POST["nPessoa"],
        descricao = request.POST["descricao"],
        total = request.POST["total"],
        data = timestamp
    ).save()

    return JsonResponse({"response": "ok", "nPessoa": request.POST["nPessoa"],
                "descricao" : request.POST["descricao"],
                "total" : request.POST["total"],
                "data" : timestamp})

def get_dados_fatura(request=None):
    import math
    print("Request",request.POST)
    fatura = Compras_View.objects.get(id = request.POST["id"])

    pessoas = Compras_View.objects.raw(f"""SELECT MIN(id) AS id, "nPessoa" FROM clicker_compras_view WHERE "nPessoa" != '{fatura.nPessoa}'  GROUP BY "nPessoa" """)
    pessoas_list = [item.nPessoa for item in pessoas]
    

    print("len->",len(pessoas),pessoas_list,pessoas)
    

    valor_a_pagar = round(int(fatura.total) / (len(pessoas)+1),2)
    #print("valor_a_pagar",valor_a_pagar)
    rounded_value = math.floor(valor_a_pagar)
    #print(pessoas_list) 


    pessoas_total = Compras_View.objects.raw(f"""SELECT MIN(id) AS id, "nPessoa" FROM clicker_compras_view WHERE "nPessoa" = '{request.POST["nPessoa"]}' GROUP BY "nPessoa" """)
    pessoa_total_dict = {}
    for pessoa in pessoas_total:
        total = 0
        faturas_pessoais = Compras_View.objects.filter(nPessoa=request.POST["nPessoa"])
        for fatura in faturas_pessoais:
            total += int(fatura.total)
        pessoa_total_dict[pessoa.nPessoa] = total # / len(pessoas)
    print(pessoa_total_dict)

    return JsonResponse({"pessoas": pessoas_list,"pessoas_qty": len(pessoas_list),"valor_a_pagar": round(valor_a_pagar,2), "total":pessoa_total_dict})

def elimina_fatura(request=None):
    print("request->",request.POST)
    fatura = Compras.objects.get(id = request.POST["id"]).delete()
    return JsonResponse({"message": "OK"})

def edita_fatura(request=None):
    print("req-> ",request.POST)
    agora = datetime.now()
    timestamp = agora.strftime('%d/%m/%Y %H:%M')
    print("request->",request.POST)
    fatura = Compras.objects.get(id = request.POST["id"])
    fatura.nPessoa = request.POST["nPessoa"]
    fatura.descricao = request.POST["descricao"]
    fatura.total = request.POST["total"]
    fatura.data = timestamp
    fatura.save()
    return JsonResponse({"message": "OK"})
    


def fechar_contas1(request=None):
    #print("Request", request.POST)
    pessoas_total = Compras_View.objects.raw("""SELECT MIN(id) AS id, "nPessoa" FROM clicker_compras_view GROUP BY "nPessoa" """)
    pessoa_total_dict = {}
    for pessoa in pessoas_total:
        total = 0
        faturas_pessoais = Compras.objects.filter(nPessoa=pessoa.nPessoa)
        for fatura in faturas_pessoais:
            total += int(fatura.total)
        pessoa_total_dict[pessoa.nPessoa] = total # / len(pessoas)
    print(pessoa_total_dict) # este dict vai ter o total que cada pessoa gastou e depois dá para dividir o total pelo numero de pessoas mas se calhar passas este valor para o front e fazes a divizão no front
    


def fechar_contas(request=None):
    #print("Request", request.POST)
    pessoas = Compras_View.objects.raw("""SELECT MIN(id) AS id, "nPessoa" FROM clicker_compras_view GROUP BY "nPessoa" """)
    pessoa_total_array = []
    
    for pessoa in pessoas:# precorrer cada pessoa
        total = 0
        faturas_pessoais = Compras_View.objects.filter(nPessoa=pessoa.nPessoa) #precorrer cada fatura de cada pessoa
        for fatura in faturas_pessoais:
            total += int(fatura.total)
        pessoa_dict = {"pessoa": pessoa.nPessoa}
        for outra_pessoa in pessoas: #precorrer de novo as pessoas para fazer o calculo de quando é que cada um lhe deve
            if outra_pessoa == pessoa:
                pessoa_dict[outra_pessoa.nPessoa] = 0.0
            else: #verificacao para não se repetir a ele proprio e precorrer todos
                pessoa_dict[outra_pessoa.nPessoa] = round(total / len(pessoas),2)  # Calcular o valor que a outra pessoa deve
        pessoa_total_array.append(pessoa_dict)
    """ 
    contas_saldadas = []
    for pessoa in pessoa_total_array:
        pessoa_saldada = {"pessoa": pessoa["pessoa"]}
        saldo_total = 0
        pessoaNome=""
        for valor in pessoa.values():
            if isinstance(valor, float) == False:
                pessoaNome=valor
            if isinstance(valor, float):
                print("valor->",pessoaNome,valor)
                saldo_total += valor
        saldo_individual = saldo_total / (len(pessoa) - 1)
        for outra_pessoa in pessoa.keys():
            if outra_pessoa != "pessoa":
                pessoa_saldada[outra_pessoa] = saldo_individual - pessoa[outra_pessoa]
    contas_saldadas.append(pessoa_saldada) """

    print(pessoa_total_array)
    return JsonResponse({"pessoas": pessoa_total_array})




#                 -------------------------FIM FUNCS COMPRAS-------------------------
