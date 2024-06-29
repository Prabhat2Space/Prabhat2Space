# Basics of UART Communication

**Date**: March 17, 2024  
**Author**: Anusha

## Outline
- Basics of UART Communication
- Brief Note on Parallel and Serial Communication
- Introduction to UART Communication
- How UART Works?
- Structure of Data Packet or Frame
- Rules of UART
- Advantages of UART
- Disadvantages of UART

## Basics of UART Communication
UART or Universal Asynchronous Receiver Transmitter is a dedicated hardware associated with serial communication. 
The hardware for UART can be a circuit integrated on the microcontroller or a dedicated IC, contrasting with SPI or I2C, which are just communication protocols.

### Applications
- GPS Receivers
- Bluetooth Modules
- GSM and GPRS Modems
- Wireless Communication Systems
- RFID based applications

## Brief Note on Parallel and Serial Communication
| Method                | Description                                                                                                    | Example Devices                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Parallel Data Transfer| All bits transferred at once using multiple wires. Fast but expensive.                                          | Old printers, RAM, PCI                |
| Serial Data Transfer  | Bits transferred one by one using a single wire. Less circuitry and cost, slower than parallel but faster now. | Modern communication devices          |

## Introduction to UART Communication
UART is a serial communication device that converts parallel data to serial data at the transmitter side and serial data to parallel data at the receiver side. 
It is universal because parameters like transfer speed, data speed, etc., are configurable.

| UART Component | Description                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Transmitting UART  | Receives parallel data from CPU, adds Start, Parity, and Stop bits, converts to serial data, transmits bit-by-bit from TX pin |
| Receiving UART     | Receives serial data at RX pin, identifies and removes Start, Parity, and Stop bits, converts to parallel data for CPU  |

## How UART Works?
UART transmits data asynchronously using special bits (Start and Stop bits) added to the actual data packet. The following table summarizes the key points:

| Component            | Function                                                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------------|
| Transmitting UART    | Receives parallel data, adds Start, Parity, Stop bits, converts to serial data, transmits from TX pin     |
| Receiving UART       | Receives serial data at RX pin, removes Start, Parity, Stop bits, converts to parallel data for CPU      |
| Start Bit            | Synchronization bit, marks beginning of data, pulls data line from high to low                           |
| Stop Bit             | Marks end of data, usually maintains data line at high                                                   |
| Parity Bit           | Optional, used for basic error checking (Even or Odd Parity)                                             |
| Data Bits            | Actual data transmitted, length between 5 and 9 bits (9 bits if no Parity, 8 bits if Parity is used)      |

## Structure of Data Packet or Frame
| Component  | Description                                                                                   |
|------------|-----------------------------------------------------------------------------------------------|
| Start Bit  | Marks the beginning of the data packet, usually one bit                                        |
| Data Bits  | Actual data, length between 5 and 9 bits                                                      |
| Parity Bit | Optional, for error checking (Even or Odd Parity)                                             |
| Stop Bit   | Marks the end of the data packet, usually one or two bits                                      |

## Rules of UART
| Rule                | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| Synchronization Bits| Start and Stop bits                                                                              |
| Parity Bit          | Optional, used for error checking (Even or Odd Parity)                                           |
| Data Bits           | Length between 5 and 9 bits                                                                      |
| Baud Rate           | Speed of data transmission, measured in bits per second (bps). Common rates: 4800, 9600, 115200 bps |

## Advantages of UART
- Requires only two wires for full duplex data transmission.
- No need for clock or other timing signals.
- Parity bit allows basic error checking.

## Disadvantages of UART
- Limited data size in the frame.
- Slower data transfer speed compared to parallel communication.
- Transmitter and receiver must agree on transmission rules and baud rate.

---

**Prabhat Shinde**  
