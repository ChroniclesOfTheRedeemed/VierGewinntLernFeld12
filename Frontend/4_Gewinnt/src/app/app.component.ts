import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { LoginPageComponent } from './login-page/login-page.component';
import { Routes } from '@angular/router';
import { MainPageComponent } from './main-page/main-page.component';
const appRoutes:Routes=[
  { path: 'Login-Page', component: LoginPageComponent },
  { path: 'Main-Page', component: MainPageComponent }
]
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = '4_Gewinnt';
  constructor(private router:Router){

  }
  
  ngOnInit(){

    this.router.navigate(['/Login-Page']);
  }
}

