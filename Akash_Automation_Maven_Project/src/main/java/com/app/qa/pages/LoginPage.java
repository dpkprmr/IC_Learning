package com.app.qa.pages;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.Assert;

import com.app.qa.base.TestBase;

public class LoginPage extends TestBase {
	
	
	public String validateLoginPage(){
		return driver.getTitle();
		
	}
	
	public boolean validateICLogo() throws IOException {
		return driver.findElement(By.xpath(datafetch(("Img")))).isDisplayed();
	}
	
	public HomePage login(String user, String pass) throws IOException {
		WebElement username = driver.findElement(By.name(datafetch(("Usernamexpath"))));
		username.sendKeys(user);
		WebElement password =  driver.findElement(By.name(datafetch(("Passwordxpath"))));
		password.sendKeys(pass);
		
		WebElement login = driver.findElement(By.xpath(datafetch(("Loginxpath"))));	
		login.click();
		return new HomePage();
		
	}
	
	
	
	
	

}
