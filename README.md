# Real-Time Delivery Tracking with Google Maps & Kafka

## Overview

# Course link - https://abhijeetgupta.graphy.com/courses/Real-Time-Delivery-Boy-Tracking-A-Hands-On-Django-and-Kafka-Integration-Course-6693c0c230423a5eedf713e2

This project showcases how to integrate Google Maps with Apache Kafka to display real-time location updates for a delivery boy. Using JavaScript, this backend system consumes and produces latitude and longitude data to update a Google Maps interface, providing live tracking of delivery activities.

The fundamentals of Kafka and Zookeeper and how they work together.
Setting up Django to work seamlessly with Kafka and Zookeeper.
Creating a project that simulates real-time vehicle location tracking, mimicking the functionalities of Uber and Zomato's delivery systems.
Step-by-step guidance on generating and handling real-time data streams.
Practical tips and best practices for building scalable, real-time applications.

## Features

- **Real-Time Location Tracking**: Visualize the delivery boy's location on Google Maps in real-time.
- **Kafka Integration**: Efficiently manage and stream location data using Apache Kafka.
- **JavaScript Backend**: Developed using JavaScript for handling backend operations and real-time data updates.

## Technologies Used

- **Google Maps API**: For real-time location visualization on maps.
- **Apache Kafka**: For streaming and processing location data.
- **Node.js**: JavaScript runtime for building and running the backend.

## Getting Started

### Prerequisites

- Node.js and npm installed on your local machine.
- A Google Maps API key. [Get your API key here](https://developers.google.com/maps/gmp-get-started).
- Apache Kafka and Zookeeper installed and running. [Kafka Installation Guide](https://kafka.apache.org/quickstart).

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/real-time-delivery-tracking.git
    cd real-time-delivery-tracking
    ```

2. **Install Dependencies**

    ```bash
    npm install
    ```

3. **Configure Google Maps API**

    - Create a `.env` file in the root directory and add your Google Maps API key:

    ```env
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```

4. **Start Kafka and Zookeeper**

    Follow the [Kafka Quickstart Guide](https://kafka.apache.org/quickstart) to start Kafka and Zookeeper.

5. **Run the Application**

    ```bash
    npm start
    ```

## Usage

1. **Producer**: Sends latitude and longitude data to Kafka topics.

2. **Consumer**: Reads data from Kafka topics and updates the Google Maps interface in real-time.

3. **Google Maps Interface**: Displays the delivery boy's current location based on the data received from Kafka.

## Example

- **Producer**: Simulates real-time data by sending location updates to Kafka at regular intervals.
- **Consumer**: Processes incoming Kafka messages and updates the map to reflect the delivery boy's location.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact:

- **Email**: abhijeetg40@gmail.com
- **GitHub**: [boxabhi](https://github.com/boxabhi)

