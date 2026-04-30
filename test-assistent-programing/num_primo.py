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

def is_prime(number: int) -> bool:
    """
    Verifica se um número é primo usando a otimização 6k±1.

    Um número primo é um número natural maior que 1 que não possui divisores
    positivos além de 1 e ele mesmo.

    Args:
        number (int): O número a ser verificado para primalidade.

    Returns:
        bool: True se o número é primo, False caso contrário.

    Raises:
        TypeError: Se a entrada não for um inteiro.
        ValueError: Se a entrada for negativa.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number < 0:
        raise ValueError("Input must be a non-negative integer")

    # Handle edge cases
    if number <= 1:
        return False
    if number <= SMALL_PRIMES_THRESHOLD:
        return True

    # Quick checks for divisibility by 2 and 3
    if _is_divisible_by_two_or_three(number):
        return False

    # Check for factors using 6k±1 optimization
    return _check_prime_factors(number)

def _is_divisible_by_two_or_three(number: int) -> bool:
    """Verifica se o número é divisível por 2 ou 3."""
    return number % 2 == 0 or number % 3 == 0

def _check_prime_factors(number: int) -> bool:
    """Verifica fatores primos usando a otimização 6k±1."""
    divisor_candidate = FIRST_PRIME_AFTER_THREE
    while divisor_candidate * divisor_candidate <= number:
        if _is_divisible_by_candidate(number, divisor_candidate):
            return False
        divisor_candidate += INCREMENT_STEP
    return True

def _is_divisible_by_candidate(number: int, candidate: int) -> bool:
    """Verifica se o número é divisível pelo candidato ou candidato + 2."""
    return number % candidate == 0 or number % (candidate + 2) == 0

def get_user_input() -> str:
    """Obtém a entrada do usuário."""
    return input(PROMPT_MESSAGE).strip().lower()

def validate_and_convert_input(user_input: str) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Valida e converte a entrada do usuário.

    Returns:
        Tuple: (is_exit, number, error_message) onde is_exit indica se o usuário
            deseja sair, number é o número inteiro convertido, e error_message
            contém a mensagem de erro, se houver.
    """
    if user_input == EXIT_COMMAND:
        return True, None, None

    try:
        number = int(user_input)
        return False, number, None
    except ValueError:
        return False, None, INVALID_INPUT_MESSAGE

def check_and_display_result(number: int) -> None:
    """Verifica se o número é primo e exibe o resultado."""
    try:
        is_prime_result = is_prime(number)
        status = "É PRIMO" if is_prime_result else "NÃO é primo"
        print(f"O número {number} {status}")
        print(RESULT_SEPARATOR)
    except (TypeError, ValueError) as error:
        print(f"❌ Erro: {error}")
        print(RESULT_SEPARATOR)

def display_welcome() -> None:
    """Exibe a mensagem de boas-vindas."""
    print(PROGRAM_TITLE)
    print("=" * SEPARATOR_LENGTH)
    print(WELCOME_MESSAGE)
    print(f"{EXIT_MESSAGE}\n")

def handle_keyboard_interrupt() -> None:
    """Trata a interrupção do teclado de forma elegante."""
    print(f"\n\n{INTERRUPTED_MESSAGE}")

def handle_unexpected_error(error: Exception) -> None:
    """Trata erros inesperados."""
    print(UNEXPECTED_ERROR_MESSAGE.format(error))
    print(RESULT_SEPARATOR)

def main() -> None:
    """Executa o verificador interativo de números primos."""
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

if __name__ == "__main__":
    main()