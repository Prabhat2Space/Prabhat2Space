# UART: A Hardware Communication Protocol Understanding Universal Asynchronous Receiver/Transmitter
---

## About UART

UART, or universal asynchronous receiver-transmitter, is one of the most used device-to-device communication protocols. 
This article explains how to use UART as a hardware communication protocol by following the standard procedure.

## Introduction

UART can work with various serial protocols, transmitting and receiving serial data bit by bit over a single line or wire. 
In two-way communication, two wires are used. Serial communication requires less circuitry and wires, reducing implementation costs.

## Fundamental Principles of UART

### Interface

UART communication involves two signals:
- **Transmitter (Tx)**
- **Receiver (Rx)**

The main purpose of the transmitter and receiver lines is to transmit and receive serial data.

### Baud Rate

The baud rate must be set the same on both the transmitting and receiving devices. 
It defines the maximum number of bits per second to be transferred.

**Table 1: UART Summary**

| Wires | Speed                                                                                                 | Methods of Transmission | Maximum Number of Masters | Maximum Number of Slaves |
|-------|-------------------------------------------------------------------------------------------------------|-------------------------|---------------------------|---------------------------|
| 2     | 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600, 1000000, 1500000                           | Asynchronous            | 1                         | 1                         |

## Data Transmission

In UART, transmission occurs in the form of packets containing a start bit, data frame, parity bit, and stop bits.

- **Start Bit**: Signals the start of data transmission.
- **Data Frame**: Contains the actual data.
- **Parity Bit**: Used for error detection.
- **Stop Bits**: Signal the end of data transmission.

## Steps of UART Transmission

1. **Transmitting UART receives data** in parallel from the data bus.
2. **Transmitting UART adds start, parity, and stop bits** to the data frame.
3. **Entire packet is sent serially** from transmitting to receiving UART.
4. **Receiving UART discards start, parity, and stop bits** from the data frame.
5. **Receiving UART converts serial data back into parallel**.

## Frame Protocol

A key feature of UART is the implementation of a frame protocol for security and protection. Designers can set unique headers, trailers, and CRC for each device.

## UART Operations

When using UART, it’s essential to check the device's data sheet and hardware reference manual.

### Steps to Follow:

1. **Check data sheet interface** of the device.
2. **Check memory map** for UART address.
3. **Check specific UART PORT details**.
4. **Check UART operation details**, including baud rate computation.
5. **Check UART configuration registers** and implement UART accordingly.

## Importance of UART

Familiarity with UART is advantageous for developing robust products. It ensures data is transferred and received without errors, providing design flexibility.
