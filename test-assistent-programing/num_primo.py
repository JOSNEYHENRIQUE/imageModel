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

def handle_keyboard_interrupt() -> None:
    """Handle keyboard interrupt gracefully."""
    print(f"\n\n{INTERRUPTED_MESSAGE}")

def handle_unexpected_error(error: Exception) -> None:
    """Handle unexpected errors."""
    print(UNEXPECTED_ERROR_MESSAGE.format(error))
    print(RESULT_SEPARATOR)

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

if __name__ == "__main__":
    main()