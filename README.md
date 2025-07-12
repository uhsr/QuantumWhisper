# QuantumWhisper: Secure Communication through Quantum-Resistant Encryption

QuantumWhisper is a Python-based library designed to provide a secure communication channel leveraging post-quantum cryptographic algorithms. In an era where quantum computing is rapidly advancing, traditional encryption methods are becoming increasingly vulnerable. This project addresses this threat by implementing and integrating advanced, quantum-resistant cryptographic primitives, ensuring the confidentiality and integrity of data transmitted through potentially compromised networks. It provides a user-friendly API for developers to seamlessly integrate quantum-resistant security into their existing applications.

This library offers a suite of features aimed at providing robust security against both classical and quantum attacks. It implements various post-quantum key exchange algorithms, digital signatures, and authenticated encryption schemes, all meticulously chosen for their resilience and performance characteristics. The project also emphasizes modularity, allowing developers to easily swap out cryptographic primitives based on their specific security requirements and performance considerations. Furthermore, QuantumWhisper includes comprehensive testing and benchmarking to ensure the correctness and efficiency of the implemented algorithms.

The primary goal of QuantumWhisper is to democratize access to post-quantum cryptography. By providing a well-documented, easy-to-use Python library, we aim to empower developers to protect their data and systems against the emerging threat of quantum computers. The library is designed to be easily integrated into various applications, ranging from secure messaging platforms to data storage solutions. With its emphasis on security, performance, and usability, QuantumWhisper is an essential tool for any organization seeking to future-proof its cryptographic infrastructure.

Key Features:

*   **CRYSTALS-Kyber Key Exchange:** Implements the CRYSTALS-Kyber key encapsulation mechanism (KEM) for secure key agreement, providing protection against quantum adversaries. The implementation utilizes the Number Theoretic Transform (NTT) for efficient polynomial multiplication.
*   **CRYSTALS-Dilithium Digital Signatures:** Provides digital signature functionality using the CRYSTALS-Dilithium algorithm, ensuring message authentication and non-repudiation even in a post-quantum environment. Includes support for different security parameter sets.
*   **AES-GCM Authenticated Encryption:** Integrates Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM) for authenticated encryption, providing both confidentiality and integrity for data transmission. This is included for hybrid security approaches.
*   **XOF-Based Mask Generation Functions (MGF):** Employs extendable output functions (XOFs) such as SHAKE128 and SHAKE256 as mask generation functions in cryptographic operations, providing enhanced security and flexibility.
*   **Modular Cryptographic Architecture:** The library is designed with a modular architecture, allowing developers to easily replace or add new cryptographic primitives as needed. This facilitates adapting to evolving security standards.
*   **Comprehensive Unit Testing:** Includes extensive unit tests to ensure the correctness and robustness of the implemented cryptographic algorithms. Tests cover all major functions and corner cases.

Technology Stack:

*   **Python 3.7+:** The core programming language used for development. We leverage Python's extensive libraries and ease of use.
*   **Cryptodome:** A powerful cryptographic library for Python, used for implementing AES-GCM and other classical cryptographic functions. Specifically, the `Crypto.Cipher` and `Crypto.Random` modules are used.
*   **NumPy:** Utilized for efficient array manipulation and numerical computation, particularly within the CRYSTALS-Kyber and CRYSTALS-Dilithium implementations.
*   **pytest:** A popular testing framework for Python, employed for running unit tests and ensuring code quality.

Installation:

1.  Clone the repository:
    `git clone https://github.com/uhsr/QuantumWhisper.git`
2.  Navigate to the project directory:
    `cd QuantumWhisper`
3.  Create a virtual environment (recommended):
    `python3 -m venv venv`
4.  Activate the virtual environment:
    `source venv/bin/activate` (Linux/macOS)
    `venv\Scripts\activate` (Windows)
5.  Install the required dependencies:
    `pip install -r requirements.txt`

Configuration:

QuantumWhisper uses environment variables for certain configurations.

*   `QUANTUMWHISPER_LOG_LEVEL`: Sets the logging level for the library. Possible values are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`. Defaults to `INFO`.
    export QUANTUMWHISPER_LOG_LEVEL=DEBUG
*   `QUANTUMWHISPER_KYBER_MODE`: Selects the Kyber implementation. Values include 'optimized' and 'reference'. The 'optimized' version is default and provides faster performance.
    export QUANTUMWHISPER_KYBER_MODE=optimized

Usage:

Example usage of the CRYSTALS-Kyber key exchange:



For API documentation, please refer to the docstrings within the Python code. Each module and function is thoroughly documented.

Contributing:

We welcome contributions to QuantumWhisper! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code.
4.  Include unit tests for your changes.
5.  Submit a pull request with a detailed description of your changes.

License:

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/QuantumWhisper/blob/main/LICENSE) file for details.

Acknowledgements:

We would like to acknowledge the researchers and developers who have contributed to the field of post-quantum cryptography. Their work has been instrumental in developing the algorithms and techniques used in QuantumWhisper. We also thank the open-source community for providing valuable resources and tools.