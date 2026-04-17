# Explicação Técnica e Didática do Código `num_primo.py` (Versão Final com Clean Code Avançado)

## O que é um Número Primo?

Um **número primo** é um número natural maior que 1 que possui apenas dois divisores positivos distintos: 1 e ele mesmo. Em outras palavras, um número primo não pode ser dividido por nenhum outro número além de 1 e si próprio sem deixar resto.

### Exemplos:
- **2** é primo (divisores: 1 e 2)
- **3** é primo (divisores: 1 e 3)
- **4** NÃO é primo (divisores: 1, 2 e 4)
- **5** é primo (divisores: 1 e 5)
- **6** NÃO é primo (divisores: 1, 2, 3 e 6)

## Algoritmo Utilizado

O código implementa uma versão otimizada do algoritmo de verificação de primalidade baseado na **otimização 6k±1**. Esta abordagem é muito mais eficiente que verificar todos os divisores possíveis até √n.

### Por que 6k±1?

Todos os números primos maiores que 3 podem ser expressos na forma **6k±1**, onde k é um número inteiro não negativo. Isso significa que os primos são da forma:
- 6k - 1 (como 5, 11, 17, 23, 29, 35...)
- 6k + 1 (como 7, 13, 19, 31, 37, 43...)

Esta propriedade permite pular muitos candidatos desnecessários durante a verificação.

## Melhorias Aplicadas (Clean Code Avançado)

Esta versão final incorpora as melhores práticas de **Clean Code** em nível avançado:

1. **Type Hints Avançados**: Uso de `Optional`, `Tuple` para tipos complexos
2. **Constantes Estruturadas**: Constantes organizadas por categoria (algoritmo, interface)
3. **Decomposição Funcional**: Funções pequenas e especializadas com responsabilidade única
4. **Separação de Responsabilidades**: Interface, validação, lógica e apresentação separadas
5. **Nomes Descritivos**: Funções privadas com `_` prefixo, nomes autoexplicativos
6. **Tratamento de Erros Robusto**: Handlers específicos para diferentes tipos de erro
7. **Interface Interativa**: Programa completo com entrada do usuário
8. **Documentação Completa**: Docstrings para todas as funções públicas

## Estrutura do Código

### Constantes Organizadas

```python
from typing import Optional, Tuple

# Constants for algorithm
FIRST_PRIME_AFTER_THREE = 5
INCREMENT_STEP = 6
SMALL_PRIMES_THRESHOLD = 3

# Constants for user interface
PROGRAM_TITLE = "Verificador de Números Primos"
SEPARATOR_LENGTH = 35
EXIT_COMMAND = "sair"
PROMPT_MESSAGE = "Digite um número: "
WELCOME_MESSAGE = "Digite um número inteiro não-negativo para verificar se é primo."
EXIT_MESSAGE = "Digite 'sair' para encerrar o programa."
GOODBYE_MESSAGE = "Programa encerrado. Até logo!"
INTERRUPTED_MESSAGE = "Programa interrompido pelo usuário. Até logo!"
INVALID_INPUT_MESSAGE = "❌ Erro: Por favor, digite apenas números inteiros ou 'sair'."
UNEXPECTED_ERROR_MESSAGE = "❌ Erro inesperado: {}"
RESULT_SEPARATOR = "-" * SEPARATOR_LENGTH
```

- **Constantes Algorítmicas**: Para a lógica matemática
- **Constantes de Interface**: Para mensagens e formatação do usuário
- **Organização**: Agrupamento lógico das constantes

### Função Principal `is_prime(number: int) -> bool`

Mantém a mesma lógica otimizada, mas agora delega tarefas para funções auxiliares.

#### Funções Auxiliares Privadas

```python
def _is_divisible_by_two_or_three(number: int) -> bool:
    """Check if number is divisible by 2 or 3."""
    return number % 2 == 0 or number % 3 == 0

def _check_prime_factors(number: int) -> bool:
    """Check for prime factors using 6k±1 optimization."""
    divisor_candidate = FIRST_PRIME_AFTER_THREE
    while divisor_candidate * divisor_candidate <= number:
        if _is_divisible_by_candidate(number, divisor_candidate):
            return False
        divisor_candidate += INCREMENT_STEP
    return True

def _is_divisible_by_candidate(number: int, candidate: int) -> bool:
    """Check if number is divisible by candidate or candidate + 2."""
    return number % candidate == 0 or number % (candidate + 2) == 0
```

- **Responsabilidade Única**: Cada função faz apenas uma coisa
- **Nomes Descritivos**: Funções privadas com prefixo `_`
- **Reutilização**: Lógica modular e testável

### Interface com o Usuário

#### Funções de Entrada e Validação

```python
def get_user_input() -> str:
    """Get input from user."""
    return input(PROMPT_MESSAGE).strip().lower()

def validate_and_convert_input(user_input: str) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Validate and convert user input.

    Returns:
        Tuple of (is_exit, number, error_message)
    """
    if user_input == EXIT_COMMAND:
        return True, None, None

    try:
        number = int(user_input)
        return False, number, None
    except ValueError:
        return False, None, INVALID_INPUT_MESSAGE
```

- **Separação de Preocupações**: Entrada, validação e conversão separadas
- **Type Hints Complexos**: Uso de `Tuple` e `Optional` para retorno múltiplo
- **Tratamento de Casos**: Comando de saída e validação de entrada

#### Funções de Saída e Exibição

```python
def check_and_display_result(number: int) -> None:
    """Check if number is prime and display result."""
    try:
        is_prime_result = is_prime(number)
        status = "É PRIMO" if is_prime_result else "NÃO é primo"
        print(f"O número {number} {status}")
        print(RESULT_SEPARATOR)
    except (TypeError, ValueError) as error:
        print(f"❌ Erro: {error}")
        print(RESULT_SEPARATOR)

def display_welcome() -> None:
    """Display welcome message."""
    print(PROGRAM_TITLE)
    print("=" * SEPARATOR_LENGTH)
    print(WELCOME_MESSAGE)
    print(f"{EXIT_MESSAGE}\n")
```

- **Exibição Consistente**: Formatação padronizada
- **Tratamento de Erros**: Captura e exibição de erros na interface

#### Handlers de Erro

```python
def handle_keyboard_interrupt() -> None:
    """Handle keyboard interrupt gracefully."""
    print(f"\n\n{INTERRUPTED_MESSAGE}")

def handle_unexpected_error(error: Exception) -> None:
    """Handle unexpected errors."""
    print(UNEXPECTED_ERROR_MESSAGE.format(error))
    print(RESULT_SEPARATOR)
```

- **Tratamento Específico**: Handlers dedicados para tipos de erro
- **Graceful Degradation**: Programa continua ou termina graciosamente

### Função `main()` - Loop Principal

```python
def main() -> None:
    """Run interactive prime checker for user input."""
    display_welcome()

    while True:
        try:
            user_input = get_user_input()
            is_exit, number, error_message = validate_and_convert_input(user_input)

            if is_exit:
                print(GOODBYE_MESSAGE)
                break

            if error_message:
                print(error_message)
                print(RESULT_SEPARATOR)
                continue

            if number is not None:
                check_and_display_result(number)

        except KeyboardInterrupt:
            handle_keyboard_interrupt()
            break
        except Exception as error:
            handle_unexpected_error(error)
```

- **Loop Estruturado**: Lógica clara de entrada-processamento-saída
- **Tratamento de Exceções**: Captura de todos os tipos de erro possíveis
- **Controle de Fluxo**: Decisões baseadas no estado da validação

## Por que isso funciona?

- **Eficiência**: Para n = 100, só verifica divisores até √100 = 10
- **Otimização**: Em vez de verificar 2,3,4,5,6,7,8,9,10... verifica apenas os candidatos prováveis (5,7,11,13,17,19...)
- **Matemática**: Baseado no fato de que todos os primos > 3 são da forma 6k±1

## Complexidade de Tempo

- **Melhor caso**: O(1) - para números pequenos ou divisíveis por 2/3
- **Caso médio**: O(√n) - proporcional à raiz quadrada do número
- **Comparação**: Algoritmo ingênuo seria O(n), este é muito mais rápido

## Vantagens desta Implementação

1. **Rápida**: Elimina candidatos desnecessários
2. **Eficiente**: Usa a propriedade matemática dos primos
3. **Limpa**: Código altamente modular e bem estruturado
4. **Robusta**: Validação completa e tratamento de erros abrangente
5. **Legível**: Nomes descritivos e constantes organizadas
6. **Testável**: Funções pequenas e independentes
7. **Interativa**: Interface completa para usuário final
8. **Manutenível**: Separação clara de responsabilidades

## Limitações

- Funciona bem para números até ~10^12 (para números maiores, algoritmos probabilísticos como Miller-Rabin são preferidos)
- Requer entrada do tipo inteiro (lança exceções para outros tipos)
- Não aceita números negativos

Esta implementação representa o ápice da aplicação de Clean Code em Python, combinando teoria matemática avançada, eficiência prática, design de software robusto e uma interface de usuário intuitiva!

### Função `is_prime(number: int) -> bool`

```python
def is_prime(number: int) -> bool:
    """
    Check if a number is prime using the 6k±1 optimization.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
```

A função agora inclui:
- **Type hints**: `number: int` e `-> bool`
- **Docstring completa**: Descrição, argumentos, retorno, exceções e exemplos
- **Exemplos**: Demonstrações práticas do uso

#### Validação de Entrada
```python
if not isinstance(number, int):
    raise TypeError("Input must be an integer")

if number < 0:
    raise ValueError("Input must be a non-negative integer")
```

- **Type checking**: Garante que a entrada seja um inteiro
- **Value validation**: Rejeita números negativos (não há primos negativos)

#### Passo 1: Casos Base
```python
# Handle edge cases
if number <= 1:
    return False
if number <= SMALL_PRIMES_THRESHOLD:
    return True
```

- Números ≤ 1 não são primos por definição
- 2 e 3 são primos (os únicos pares e ímpares pequenos)
- Usa constante `SMALL_PRIMES_THRESHOLD` em vez de número mágico

#### Passo 2: Verificações Rápidas
```python
# Quick checks for divisibility by 2 and 3
if number % 2 == 0 or number % 3 == 0:
    return False
```

- Se `number` é divisível por 2 ou 3, não é primo
- Isso elimina a maioria dos números compostos rapidamente

#### Passo 3: Loop de Verificação Otimizado
```python
# Check for factors using 6k±1 optimization
divisor_candidate = FIRST_PRIME_AFTER_THREE
while divisor_candidate * divisor_candidate <= number:
    if number % divisor_candidate == 0 or number % (divisor_candidate + 2) == 0:
        return False
    divisor_candidate += INCREMENT_STEP
return True
```

Este é o coração do algoritmo:

1. **Inicialização**: Começa com `divisor_candidate = FIRST_PRIME_AFTER_THREE` (5)
2. **Condição do loop**: `divisor_candidate * divisor_candidate <= number` - só verifica até a raiz quadrada
3. **Verificação**: Testa se number é divisível por `divisor_candidate` ou `divisor_candidate + 2`
4. **Incremento**: `divisor_candidate += INCREMENT_STEP` - pula para o próximo par de candidatos (6k±1)

### Função `main()`

```python
def main() -> None:
    """Run interactive prime checker for user input."""
    print("Verificador de Números Primos")
    print("=" * 35)
    print("Digite um número inteiro não-negativo para verificar se é primo.")
    print("Digite 'sair' para encerrar o programa.\n")
    
    while True:
        try:
            user_input = input("Digite um número: ").strip().lower()
            
            if user_input == 'sair':
                print("Programa encerrado. Até logo!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Check if prime
            result = is_prime(number)
            status = "É PRIMO" if result else "NÃO é primo"
            
            print(f"O número {number} {status}")
            print("-" * 35)
            
        except ValueError as e:
            if "invalid literal" in str(e):
                print("❌ Erro: Por favor, digite apenas números inteiros ou 'sair'.")
            else:
                print(f"❌ Erro: {e}")
            print("-" * 35)
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            print("-" * 35)
```

A função `main()` agora implementa uma **interface interativa**:

- **Loop infinito**: Permite múltiplas verificações sem reiniciar o programa
- **Entrada do usuário**: Solicita números via `input()`
- **Tratamento de entrada**: Converte string para inteiro e trata erros
- **Opção de saída**: Comando 'sair' para encerrar graciosamente
- **Tratamento de exceções**: Captura erros de conversão, interrupção e outros
- **Feedback visual**: Emojis e formatação para melhor experiência do usuário

#### Tratamento de Entrada Inválida

- **Conversão segura**: `int(user_input)` pode lançar `ValueError`
- **Mensagens claras**: Indica especificamente o tipo de erro
- **Recuperação**: Continua executando após erros em vez de crash
- **Interrupção**: `Ctrl+C` permite saída elegante

### Por que isso funciona?

- **Eficiência**: Para n = 100, só verifica divisores até √100 = 10
- **Otimização**: Em vez de verificar 2,3,4,5,6,7,8,9,10... verifica apenas os candidatos prováveis (5,7,11,13,17,19...)
- **Matemática**: Baseado no fato de que todos os primos > 3 são da forma 6k±1

## Seção de Interação com Usuário

```python
if __name__ == "__main__":
    main()
```

Esta seção só executa quando o arquivo é rodado diretamente (não quando importado como módulo). Inicia a interface interativa que permite ao usuário verificar múltiplos números consecutivamente.

### Como Usar:

1. **Execute o programa**: `python num_primo.py`
2. **Digite um número**: Qualquer inteiro não-negativo
3. **Veja o resultado**: O programa informa se é primo ou não
4. **Continue testando**: Digite outro número ou 'sair' para encerrar

### Exemplo de Uso:

```
Verificador de Números Primos
===================================
Digite um número inteiro não-negativo para verificar se é primo.
Digite 'sair' para encerrar o programa.

Digite um número: 17
O número 17 É PRIMO
-----------------------------------
Digite um número: 18
O número 18 NÃO é primo
-----------------------------------
Digite um número: sair
Programa encerrado. Até logo!
```

## Complexidade de Tempo

- **Melhor caso**: O(1) - para números pequenos ou divisíveis por 2/3
- **Caso médio**: O(√n) - proporcional à raiz quadrada do número
- **Comparação**: Algoritmo ingênuo seria O(n), este é muito mais rápido

## Vantagens desta Implementação

1. **Rápida**: Elimina candidatos desnecessários
2. **Eficiente**: Usa a propriedade matemática dos primos
3. **Limpa**: Código bem estruturado e documentado
4. **Robusta**: Validação de entrada e tratamento de erros
5. **Legível**: Nomes significativos e constantes descritivas
6. **Testável**: Função separada para testes

## Limitações

- Funciona bem para números até ~10^12 (para números maiores, algoritmos probabilísticos como Miller-Rabin são preferidos)
- Requer entrada do tipo inteiro (lança exceções para outros tipos)
- Não aceita números negativos

Esta implementação combina teoria matemática avançada, eficiência prática e as melhores práticas de desenvolvimento em Python!