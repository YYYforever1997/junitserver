package com.trustie.test;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.Test;
import com.trustie.junitest.calculate;

public class calculatetest{
	calculate calculation = new calculate();
	int sum = calculation.sum(8,2);
	int testSum = 10;

	@Test
	public void testSum(){
		System.out.println("@Test sum():"+sum+"="+testSum+"\n");
		assertEquals(sum,testSum);
		System.out.println("calculatetest1 finished!\n");
	}
}

