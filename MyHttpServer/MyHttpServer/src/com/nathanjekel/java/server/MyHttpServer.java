package com.nathanjekel.java.server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;

public class MyHttpServer {

	//
	// Argument 1: Host
	// Argument 2: Port
	public static void main(String[] args) {
		String host = args[0];
		Integer port = new Integer(args[1]);
		
		try(ServerSocket serverSocket = new ServerSocket()) {
			bindToClientSocket(serverSocket, host, port);
			
			while(true) {
				Socket client = serverSocket.accept();
				readRequest(client);
				sendResponse(client);
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		}

	}
	
	private static void bindToClientSocket(ServerSocket serverSocket, String host, int port) throws IOException {
		InetSocketAddress socketAddress = new InetSocketAddress(host, port);
		serverSocket.bind(socketAddress);
		System.out.println("Serving HTTP on port " + port + "...");
	}
	
	private static void readRequest(Socket client) throws IOException {
		InputStreamReader inputStreamReader = new InputStreamReader(client.getInputStream());
		BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
		String inputLine = bufferedReader.readLine(); 
		
		while (!inputLine.isEmpty()) { 
			System.out.println(inputLine); 
			inputLine = bufferedReader.readLine();
		}
	}
	
	private static void sendResponse(Socket client) throws IOException {
	    String response = "HTTP/1.1 200 OK\n\n Hello, World!";
	    client.getOutputStream().write(response.getBytes());
	    client.close();
	}

}
