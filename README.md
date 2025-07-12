# QuantumWhisper: Decentralized Price Anomaly Detection for Crypto Assets

QuantumWhisper is a pioneering project that leverages blockchain technology and serverless computing to provide a decentralized and near real-time price anomaly detection system for cryptocurrency assets. It detects unusual price movements and triggers alerts, enabling timely responses to potential market manipulation, flash crashes, or arbitrage opportunities.

This system aims to address the limitations of centralized anomaly detection solutions, which are prone to single points of failure and lack transparency. QuantumWhisper distributes the anomaly detection logic across a smart contract deployed on a compatible blockchain network (e.g., Ethereum, Polygon), making it resistant to censorship and manipulation. When a price anomaly is detected by the smart contract, it emits an event which is then captured by a serverless function. This function processes the event data and sends alerts via various channels, such as email, SMS, or webhook integrations. This architecture provides a scalable, reliable, and tamper-proof method for monitoring cryptocurrency markets.

QuantumWhisper provides several key benefits. It offers a decentralized and transparent anomaly detection mechanism, increasing trust and security. The near real-time alert system ensures timely notifications of potentially critical market events. The serverless function architecture allows for high scalability and cost-effectiveness, as resources are only consumed when anomalies are detected. Finally, the system is designed to be highly configurable, allowing users to define their own anomaly detection parameters and alert preferences.

## Key Features

*   **On-Chain Anomaly Detection:** Smart contracts written in Solidity implement a moving average deviation algorithm to detect price anomalies based on configurable thresholds and lookback periods. The contract stores a history of recent price data and calculates deviations from the moving average in real-time.
*   **Event-Driven Architecture:** The smart contract emits events when a price anomaly is detected, including the asset symbol, timestamp, current price, and deviation percentage. These events serve as triggers for the serverless alert system.
*   **Serverless Alert Processing:** A serverless function (e.g., AWS Lambda, Google Cloud Functions) subscribes to the smart contract events and processes the anomaly data. This function filters alerts based on user-defined preferences and formats the alert message.
*   **Multi-Channel Alert Delivery:** The serverless function integrates with various notification services (e.g., Twilio, SendGrid, Slack) to deliver alerts via email, SMS, or webhook integrations. Users can customize their preferred alert channels and notification frequency.
*   **Configurable Anomaly Thresholds:** Users can configure the anomaly detection thresholds directly within the smart contract, allowing them to fine-tune the sensitivity of the system based on their risk tolerance and trading strategies. Parameters include deviation percentage, lookback window, and minimum trading volume.
*   **Historical Data Analysis:** An accompanying Python script allows for analysis of historical price data to determine optimal anomaly detection thresholds. This script retrieves data from a cryptocurrency exchange API and simulates the smart contract's anomaly detection algorithm.
*   **Decentralized Governance (Future):** Plans are in place to implement a decentralized governance mechanism, allowing token holders to vote on changes to the anomaly detection algorithm and other system parameters.

## Technology Stack

*   **Solidity:** Smart contract language for implementing the on-chain anomaly detection logic.
*   **Ethereum (or compatible blockchain):** Blockchain platform for deploying and executing the smart contract.
*   **Python:** Used for scripting, data analysis, and interacting with blockchain APIs. Libraries include Web3.py for interacting with the Ethereum blockchain and Pandas for data manipulation.
*   **Web3.py:** Python library for interacting with the Ethereum blockchain, used for deploying the smart contract, retrieving events, and managing accounts.
*   **AWS Lambda (or similar serverless platform):** Serverless computing platform for processing anomaly events and sending alerts.
*   **Twilio/SendGrid/Slack APIs:** APIs for sending SMS, email, or Slack notifications.

## Installation

1.  Clone the repository:
    git clone https://github.com/uhsr/QuantumWhisper.git
    cd QuantumWhisper

2.  Install Python dependencies:
    pip install -r requirements.txt

3.  Install Ganache (for local blockchain development):
    npm install -g ganache-cli

4.  Install Truffle (for smart contract deployment):
    npm install -g truffle

## Configuration

1.  Set environment variables:
    Create a `.env` file in the root directory with the following variables:
    ALCHEMY_API_KEY=<Your Alchemy API Key>
    PRIVATE_KEY=<Your Ethereum Private Key>
    TWILIO_ACCOUNT_SID=<Your Twilio Account SID>
    TWILIO_AUTH_TOKEN=<Your Twilio Auth Token>
    TWILIO_PHONE_NUMBER=<Your Twilio Phone Number>
    RECIPIENT_PHONE_NUMBER=<Recipient Phone Number for Alerts>

2.  Configure the smart contract:
    Modify the `truffle-config.js` file to specify the network configuration (e.g., development, mainnet, rinkeby).

3.  Configure the serverless function:
    Set environment variables for the serverless function (e.g., AWS Lambda) to match the `.env` file.

## Usage

1.  Deploy the smart contract:
    truffle compile
    truffle migrate --network development

2.  Run the historical data analysis script:
    python scripts/analyze_historical_data.py --symbol BTCUSDT --lookback 14 --deviation 0.05

3.  Deploy the serverless function:
    Package and deploy the serverless function code to your chosen platform (e.g., AWS Lambda). Configure the function to subscribe to the smart contract events.

4.  Test the system:
    Manually trigger a price anomaly (e.g., by sending a large transaction to the smart contract) and verify that an alert is received via the configured notification channel.

## Contributing

We welcome contributions to QuantumWhisper! Please follow these guidelines:

*   Fork the repository and create a branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Adhere to the project's coding style and conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/QuantumWhisper/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for providing the tools and libraries that made this project possible.