package com.app.qa.pages;

import java.io.IOException;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.app.qa.base.TestBase;

public class HomePage extends TestBase {
	
	public String validateHomePage() {
		return driver.getTitle();
		
	}
	
	public boolean validateICLogo() throws IOException {
		return driver.findElement(By.xpath(datafetch(("Img1")))).isDisplayed();
	}
	
	public boolean validateCompareSnapshotbutton() throws IOException {
		return driver.findElement(By.xpath(datafetch(("Cmp_button")))).isDisplayed();
	}
	

}
