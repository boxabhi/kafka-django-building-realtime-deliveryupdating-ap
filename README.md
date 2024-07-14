# 🚀 Real-Time Delivery Tracking with Google Maps & Kafka 🚀

## Overview

This project demonstrates how to seamlessly integrate **Google Maps** with **Apache Kafka** to enable real-time location tracking for a delivery boy. By leveraging **Django**, the backend system effectively consumes and produces latitude and longitude data, updating the **Google Maps** interface to provide live tracking of delivery activities. 

In this **advanced project tutorial**, you'll learn how to integrate **Kafka with Django**, a crucial skill for mastering real-time data processing and web application development. This video is perfect for those who wish to enhance their Django skills through **project-based learning**. Whether you're looking to advance your backend development expertise or want to implement live tracking features, this video provides a comprehensive guide to achieving that goal.

🎓 **Check out the full course here:** [Real-Time Delivery Boy Tracking: A Hands-On Django and Kafka Integration Course](https://abhijeetgupta.graphy.com/courses/Real-Time-Delivery-Boy-Tracking-A-Hands-On-Django-and-Kafka-Integration-Course-6693c0c230423a5eedf713e2)

## Features

- **Real-Time Location Tracking**: Visualize the delivery boy's location on Google Maps in real-time.
- **Kafka Integration**: Efficiently manage and stream location data using Apache Kafka.
- **Django Backend**: Developed using Django for handling backend operations and real-time data updates.

## Technologies Used

- **Google Maps API**: For real-time location visualization on maps.
- **Apache Kafka**: For streaming and processing location data.
- **Django**: Web framework for backend development.

## Getting Started

### Prerequisites

- Python and Django installed on your local machine.
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
    pip install -r requirements.txt
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
    python manage.py runserver
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

- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

