import mysql.connector
from time import sleep


# ============================================================
# TIPOS DE CONTAINER
# ============================================================

ISOS_VALIDOS = {

    # -------------------------
    # DRY / GENERAL PURPOSE
    # -------------------------

    "22G1": {
        "tipo": "DRY",
        "tamanho": "20DC",
        "descricao": "20 PÉS STANDARD DRY"
    },

    "42G1": {
        "tipo": "DRY",
        "tamanho": "40DC",
        "descricao": "40 PÉS STANDARD DRY"
    },

    "45G1": {
        "tipo": "DRY",
        "tamanho": "40HC",
        "descricao": "40 PÉS HIGH CUBE DRY"
    },


    # -------------------------
    # REEFER
    # -------------------------

    "22R1": {
        "tipo": "REEFER",
        "tamanho": "20RF",
        "descricao": "20 PÉS REEFER",
        "refrigerado": True
    },

    "42R1": {
        "tipo": "REEFER",
        "tamanho": "40RF",
        "descricao": "40 PÉS REEFER",
        "refrigerado": True
    },

    "45R1": {
        "tipo": "REEFER",
        "tamanho": "40HR",
        "descricao": "40 PÉS HIGH CUBE REEFER",
        "refrigerado": True
    },


    # -------------------------
    # OPEN TOP
    # -------------------------

    "22U1": {
        "tipo": "OPEN TOP",
        "tamanho": "20OT",
        "descricao": "20 PÉS OPEN TOP"
    },

    "42U1": {
        "tipo": "OPEN TOP",
        "tamanho": "40OT",
        "descricao": "40 PÉS OPEN TOP"
    },

    "45U1": {
        "tipo": "OPEN TOP",
        "tamanho": "40HC OT",
        "descricao": "40 PÉS HIGH CUBE OPEN TOP"
    },


    # -------------------------
    # FLAT RACK
    # -------------------------

    "22P1": {
        "tipo": "FLAT RACK",
        "tamanho": "20FR",
        "descricao": "20 PÉS FLAT RACK FIXED ENDS"
    },

    "42P1": {
        "tipo": "FLAT RACK",
        "tamanho": "40FR",
        "descricao": "40 PÉS FLAT RACK FIXED ENDS"
    },

    "22P3": {
        "tipo": "FLAT RACK",
        "tamanho": "20FR",
        "descricao": "20 PÉS FLAT RACK COLLAPSIBLE"
    },

    "42P3": {
        "tipo": "FLAT RACK",
        "tamanho": "40FR",
        "descricao": "40 PÉS FLAT RACK COLLAPSIBLE"
    },

    "45P3": {
        "tipo": "FLAT RACK",
        "tamanho": "40HC FR",
        "descricao": "40 PÉS HIGH CUBE FLAT RACK"
    },


    # -------------------------
    # TANK
    # -------------------------

    "22T0": {
        "tipo": "TANK",
        "tamanho": "20TK",
        "descricao": "20 PÉS TANK - LÍQUIDO NÃO PERIGOSO"
    },

    "22T1": {
        "tipo": "TANK",
        "tamanho": "20TK",
        "descricao": "20 PÉS TANK"
    },

    "22T5": {
        "tipo": "TANK",
        "tamanho": "20TK",
        "descricao": "20 PÉS TANK - LÍQUIDO PERIGOSO"
    },

    "22T6": {
        "tipo": "TANK",
        "tamanho": "20TK",
        "descricao": "20 PÉS TANK - LÍQUIDO PERIGOSO"
    },

    "42T2": {
        "tipo": "TANK",
        "tamanho": "40TK",
        "descricao": "40 PÉS TANK"
    },


    # -------------------------
    # BULK
    # -------------------------

    "22B0": {
        "tipo": "BULK",
        "tamanho": "20BK",
        "descricao": "20 PÉS BULK"
    },

    "45B3": {
        "tipo": "BULK",
        "tamanho": "40HC BK",
        "descricao": "40 PÉS HIGH CUBE BULK"
    },


    # -------------------------
    # PLATFORM
    # -------------------------

    "49P0": {
        "tipo": "PLATFORM",
        "tamanho": "40PL",
        "descricao": "40 PÉS PLATFORM"
    }
}


# ============================================================
# CONEXÃO MYSQL
# ============================================================

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cadastro"
)

cursor = conexao.cursor()


# ============================================================
# FUNÇÃO - VALIDAR NÚMERO DO CONTAINER
# ============================================================

def validar_container(numero):

    numero = numero.strip().upper()

    if len(numero) != 11:
        return False

    # 4 primeiras posições = letras
    if not numero[:4].isalpha():
        return False

    # 7 últimas posições = números
    if not numero[4:].isdigit():
        return False

    return True


# ============================================================
# FUNÇÃO - VALIDAR ISO
# ============================================================

def validar_iso(iso):

    return iso in ISOS_VALIDOS


# ============================================================
# FUNÇÃO - VALIDAR TARA
# ============================================================

def validar_tara(tara):

    if tara <= 0:
        return False

    return True


# ============================================================
# FUNÇÃO - VALIDAR MAX GROSS
# ============================================================

def validar_mgw(mgw, tara):

    if mgw <= 0:
        return False

    if mgw <= tara:
        return False

    return True


# ============================================================
# FUNÇÃO - MOSTRAR ISOS
# ============================================================

def mostrar_isos():

    print("\n" + "=" * 70)
    print("                    ISOS DISPONÍVEIS")
    print("=" * 70)

    for iso, dados in ISOS_VALIDOS.items():

        print(
            f"{iso:<6} | "
            f"{dados['tipo']:<12} | "
            f"{dados['tamanho']:<10} | "
            f"{dados['descricao']}"
        )

    print("=" * 70)


# ============================================================
# INÍCIO DO SISTEMA
# ============================================================

print("\n" + "=" * 60)
print("             SISTEMA DE CADASTRO DE CONTAINERS")
print("=" * 60)


while True:

    # ========================================================
    # NÚMERO DO CONTAINER
    # ========================================================

    while True:

        numero = input(
            "\nDigite o número do container: "
        ).strip().upper()

        if validar_container(numero):
            break

        print(
            "ERRO: número de container inválido."
        )

        print(
            "Exemplo de formato: ABCD1234567"
        )


    # ========================================================
    # ISO
    # ========================================================

    mostrar_isos()

    while True:

        iso = input(
            "\nDigite o ISO do container: "
        ).strip().upper()

        if validar_iso(iso):
            break

        print(
            "\nERRO: ISO inválido."
        )

        print(
            "Digite um dos códigos apresentados acima."
        )


    # ========================================================
    # INFORMAÇÕES DO ISO
    # ========================================================

    dados_iso = ISOS_VALIDOS[iso]

    tipo = dados_iso["tipo"]
    tamanho = dados_iso["tamanho"]
    descricao = dados_iso["descricao"]

    
    # ========================================================
    # SITUAÇÃO
    # ========================================================

    while True:

        situacao = input(
            "\nContainer CHEIO ou VAZIO? "
        ).strip().upper()

        if situacao in ["CHEIO", "VAZIO"]:
            break

        print(
            "ERRO: digite CHEIO ou VAZIO."
        )

    # ========================================================
    # TEMPERATURA - REEFER
    # ========================================================

    temperatura = None

    # Só pede temperatura se:
    # 1. O cntr for REEFEER
    # 2. O cntr estiver CHEIO

    if dados_iso.get("refrigerado") and situacao == "CHEIO":

        print(
            "\nContainer REEFER CHEIO identificado."
        )

        while True:

            try:

                temperatura = float(
                    input(
                        "Digite a temperatura do container (°C): "
                    )
                )

                # Exemplo de limite operacional.
                # Pode ser ajustado conforme a regra do terminal.

                if temperatura < -40 or temperatura > 30:

                    print(
                        "ERRO: temperatura fora do intervalo "
                        "permitido (-40°C até 30°C)."
                    )

                else:
                    break

            except ValueError:

                print(
                    "ERRO: digite uma temperatura válida."
                )
    elif dados_iso.get("refrigerado") and situacao == "VAZIO":
        print(
            "\nContainer REEFER VAZIO."
        )
        print(
            "Temperatura não será solicitada."
        )
    # ========================================================
    # TARA
    # ========================================================

    while True:

        try:

            tara = int(
                input(
                    "\nDigite a TARA do container (kg): "
                )
            )

            if validar_tara(tara):
                break

            print(
                "ERRO: a tara deve ser maior que zero."
            )

        except ValueError:

            print(
                "ERRO: digite somente números."
            )


    # ========================================================
    # MAX GROSS
    # ========================================================

    while True:

        try:

            mgw = int(
                input(
                    "Digite o MAX GROSS / MGW (kg): "
                )
            )

            if validar_mgw(mgw, tara):
                break

            print(
                "\nERRO: MAX GROSS inválido."
            )

            print(
                "O MAX GROSS precisa ser maior que a tara."
            )

        except ValueError:

            print(
                "ERRO: digite somente números."
            )


    # ========================================================
    # RESUMO
    # ========================================================

    print("\n" + "=" * 60)
    print("                 RESUMO DO CONTAINER")
    print("=" * 60)

    print(f"CONTAINER : {numero}")
    print(f"ISO       : {iso}")
    print(f"TIPO      : {tipo}")
    print(f"TAMANHO   : {tamanho}")
    print(f"DESCRIÇÃO : {descricao}")
    print(f"TARA      : {tara} kg")
    print(f"MAX GROSS : {mgw} kg")

    if temperatura is not None:

        print(
            f"TEMPERATURA: {temperatura} °C"
        )

    print(f"SITUAÇÃO  : {situacao}")

    print("=" * 60)


    # ========================================================
    # CONFIRMAÇÃO
    # ========================================================

    while True:

        confirmar = input(
            "\nDeseja confirmar o cadastro? [S/N]: "
        ).strip().upper()

        if confirmar in ["S", "N"]:
            break

        print(
            "Digite apenas S ou N."
        )


    if confirmar == "S":

        cursor.execute(
            """
            INSERT INTO containers
            (numero, iso, tara, mgw, temp, situacao, tamanho)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                numero,
                iso,
                tara,
                mgw,
                temperatura,
                situacao,
                tamanho
            )
        )

        conexao.commit()

        print("\nAguarde...")
        sleep(1)

        print(
            "\nCONTAINER CADASTRADO COM SUCESSO!"
        )

        break

    else:

        print(
            "\nCadastro cancelado."
        )

        break


# ============================================================
# ENCERRAMENTO
# ============================================================

cursor.close()
conexao.close()

print("\nSistema encerrado.")