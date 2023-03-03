import { Component, Input } from '@angular/core';
import { Router, Routes } from '@angular/router';
import { MainPageComponent } from '../main-page/main-page.component';
import { NetworkBackendComponent } from '../network-backend/network-backend.component';
import { HttpClient } from '@angular/common/http';
import { async } from 'rxjs';
import { UserCreationComponent } from '../user-creation/user-creation.component';
const appRoutes:Routes=[
  { path: 'Main-Page', component: MainPageComponent },
  { path: 'User-Creation', component: UserCreationComponent }
]

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent {
  constructor(public router:Router, public network:NetworkBackendComponent){

  }
  userCreation(){
    this.router.navigate(['/User-Creation']);
  }
   onSelect( User:String, psw:String) {
    
    console.log(User,psw+" test")
     this.network.Autherisation(User,psw);

    
  }

    
  

}
