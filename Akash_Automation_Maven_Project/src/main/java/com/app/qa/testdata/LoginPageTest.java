package com.app.qa.testdata;

import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import com.app.qa.base.TestBase;
import com.app.qa.pages.HomePage;
import com.app.qa.pages.LoginPage;

public class LoginPageTest extends TestBase{
	
	LoginPage loginpage;
	HomePage homepage;
	Properties prop;
	
	
	@BeforeTest
	public void setup() throws IOException {
		initialization();
		 loginpage = new LoginPage();
	}
	
	
	@Test
	public void ICLogoTest() throws IOException {
		 boolean flag = loginpage.validateICLogo();
		Assert.assertTrue(flag);
	}
	
	@Test
	public void loginPageTitleTest() {
		String title = loginpage.validateLoginPage();
		Assert.assertEquals(title, "ICyte Login");
		
	}

	@Test
	public void LoginTest() throws IOException, InterruptedException {
		homepage = loginpage.login(datafetch(("UserName")), datafetch(("Password")));
	}
	
	
	@AfterTest
	public void closeBrwser() {
		driver.close();
	}
	
	
}
