# Projeto Joia - Test Assistant Programming

Um conjunto de programas educacionais em Python demonstrando boas práticas de programação, otimizações algorítmicas e refatoração de código.

## 📋 Visão Geral

Este projeto contém três módulos principais que ilustram diferentes conceitos de programação profissional:

- **Verificador de Números Primos** - Implementação otimizada com Clean Code avançado
- **Sistema de Cálculo de Faturas** - Lógica de negócio com tratamento de desconto e imposto
- **Refatoração de Código** - Comparação entre código legado e código refatorado

---

## 🎯 Módulos

### 1. **num_primo.py** - Verificador de Números Primos

Um programa interativo que verifica se um número é primo usando a otimização **6k±1**.

#### Características:
- ✅ Algoritmo otimizado para verificação rápida de primalidade
- ✅ Type hints completos com tipos complexos (`Optional`, `Tuple`)
- ✅ Constantes organizadas por categoria (algoritmo e interface)
- ✅ Decomposição funcional com responsabilidade única
- ✅ Tratamento robusto de erros
- ✅ Interface interativa com usuário
- ✅ Docstrings em estilo Google (português)

#### Como Executar:
```bash
python num_primo.py
```

#### Exemplo de Uso:
```
Verificador de Números Primos
===================================
Digite um número inteiro não-negativo para verificar se é primo.
Digite 'sair' para encerrar o programa.

Digite um número: 17
O número 17 É PRIMO
---------------------------------

Digite um número: 24
O número 24 NÃO é primo
---------------------------------

Digite um número: sair
Programa encerrado. Até logo!
```

#### O Algoritmo:
Todos os números primos maiores que 3 seguem o padrão **6k±1**:
- Forma: 6k - 1 (ex: 5, 11, 17, 23, 29...)
- Forma: 6k + 1 (ex: 7, 13, 19, 31, 37...)

Isso permite pular muitos candidatos desnecessários, tornando a verificação muito mais eficiente.

#### Funções Principais:
- `is_prime(number: int) -> bool` - Verifica primalidade
- `validate_and_convert_input(user_input: str)` - Valida entrada do usuário
- `check_and_display_result(number: int)` - Exibe resultado
- `main()` - Loop principal interativo

---

### 2. **debug.py** - Sistema de Cálculo de Faturas

Um programa que calcula o total de uma compra com múltiplos itens, aplicando impostos e descontos.

#### Características:
- ✅ Entrada de dados de cliente e itens
- ✅ Cálculo de subtotal por item
- ✅ Aplicação automática de imposto (10%)
- ✅ Suporte a cupom de desconto (percentual)
- ✅ Formatação profissional de fatura
- ✅ Exibição condicional de desconto
- ✅ Comentários inline explicando decisões lógicas

#### Como Executar:
```bash
python debug.py
```

#### Exemplo de Uso:
```
==============================
 Cliente: João Silva
==============================
 Item 1:        R$ 50.00
 Item 2:        R$ 30.00
 Item 3:        R$ 20.00
------------------------------
 Subtotal:      R$ 100.00
 Imposto (10%): R$ 10.00
 Desconto (15%): -R$ 15.00
==============================
 TOTAL:         R$ 95.00
==============================
```

#### Fluxo de Cálculo:
1. Coleta dados do cliente (nome, quantidades e preços)
2. Calcula total de cada item
3. Calcula subtotal (soma de todos os itens)
4. Aplica imposto fixo de 10% sobre o subtotal
5. Solicita cupom de desconto (opcional)
6. Exibe fatura formatada com todos os valores

---

### 3. **refatoracao.py** - Exemplo de Refatoração

Demonstra como transformar código legado e pouco legível em código profissional seguindo PEP 8 e boas práticas.

#### Problema Original:
```python
# ❌ Código com problemas
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    # ... mais código com variáveis confusas
```

#### Solução Refatorada:
```python
# ✅ Código refatorado
def calculate_list_statistics(numbers):
    """
    Calculate the total, mean, maximum, and minimum of a list of numbers.
    """
    total = 0
    for number in numbers:
        total += number
    mean = total / len(numbers)
    # ... código legível com nomes descritivos
```

#### Melhorias Aplicadas:
- 🔹 Nomes descritivos para funções e variáveis
- 🔹 Docstrings completas
- 🔹 Remoção de índices desnecessários
- 🔹 Conformidade com PEP 8
- 🔹 Maior legibilidade e manutenibilidade

#### Como Executar:
```bash
python refatoracao.py
```

---

## 📚 Documentação Adicional

### Arquivos de Explicação:

#### `explicacao_num_primo.md`
Explicação técnica e didática sobre:
- O que é um número primo
- O algoritmo 6k±1 e por que funciona
- Melhorias aplicadas em Clean Code avançado
- Estrutura completa do código

#### `explicacao_refatoracao.md`
Análise detalhada sobre:
- Problemas do código original
- Comparação antes e depois
- Benefícios da refatoração
- Convenções de código (PEP 8)

---

## 🛠️ Requisitos

- Python 3.7+

Nenhuma dependência externa necessária.

---

## 💡 Conceitos Abordados

### Clean Code Avançado
- Type hints
- Constantes organizadas
- Decomposição funcional
- Separação de responsabilidades
- Nomes descritivos
- Tratamento de erros robusto

### Boas Práticas Python
- PEP 8 (estilo)
- Docstrings em formato Google (português)
- Uso de funções privadas (prefixo `_`)
- Padrões de design (separação de interface, validação, lógica)

### Otimizações Algorítmicas
- Algoritmo 6k±1 para verificação de primalidade
- Redução de iterações desnecessárias
- Cálculo eficiente de complexidade

---

## 🎓 Uso Educacional

Este projeto é ideal para:
- Estudantes aprendendo Python
- Desenvolvedores em transição para código profissional
- Equipes que desejam entender padrões de Clean Code
- Revisão de conceitos algorítmicos

---

## 📝 Estrutura de Arquivos

```
test-assistent-programing/
├── README.md                      # Este arquivo
├── num_primo.py                   # Verificador de números primos
├── debug.py                       # Sistema de cálculo de faturas
├── refatoracao.py                 # Exemplo de refatoração
├── explicacao_num_primo.md        # Documentação técnica (primos)
└── explicacao_refatoracao.md      # Documentação técnica (refatoração)
```

---

## ✨ Destaques

| Aspecto | Detalhe |
|---------|---------|
| **Linguagem** | Python 3.7+ |
| **Padrão de Código** | PEP 8 + Clean Code |
| **Type Hints** | Completos em todas as funções |
| **Documentação** | Docstrings em Google Style (português) |
| **Tratamento de Erros** | Robusto com exceptions específicas |
| **Interface** | Interativa com feedback ao usuário |

---

## 🚀 Próximos Passos Sugeridos

1. Estudar e executar cada módulo
2. Modificar os programas para entender melhor
3. Criar testes unitários para as funções
4. Refatorar o `debug.py` usando funções e classes
5. Implementar variações dos algoritmos

---

## 📄 Licença

Este projeto é fornecido para fins educacionais.

---

**Desenvolvido com ❤️ para aprendizado de programação Python profissional**
