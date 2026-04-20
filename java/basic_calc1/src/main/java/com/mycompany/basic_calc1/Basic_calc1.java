/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.basic_calc1;

import java.util.Scanner;

/**
 *
 * @author Estudiantes
 */
public class Basic_calc1 {

    public static void main(String[] args) {
        float num1=0, num2=0, add=0;
        int opt=0;
        
        Scanner scanner =new Scanner(System.in);  
        
        System.out.println("::: MY BASIC CALC :::");
        System.out.println("Enter first number: ");
        num1 = scanner.nextFloat();
        System.out.println("Enter second number: ");
        num2 = scanner.nextFloat();
        
        System.out.println(""
                + "[1]. Addition\n" 
                + "[2]. Substraction\n"
                + "[3]. Multiplication\n"
                + "[4]. Division\n"
                + "[5]. Average\n"
                + "[6]. All options\n");
        opt = scanner.nextInt();
  
        if (opt==1){
            add= num1 + num2;
            System.out.println("Addition is: " + (num1 + num2));
        }else{
    }
}
