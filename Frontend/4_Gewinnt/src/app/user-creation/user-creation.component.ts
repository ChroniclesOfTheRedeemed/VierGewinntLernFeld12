import { Component, Input } from '@angular/core';
import { Router, Routes } from '@angular/router';
import { NetworkBackendComponent } from '../network-backend/network-backend.component';


@Component({
  selector: 'app-user-creation',
  templateUrl: './user-creation.component.html',
  styleUrls: ['./user-creation.component.css']
})
export class UserCreationComponent {
  constructor(public router:Router, public network:NetworkBackendComponent){}
  userCreation(User:String, psw:String,pswbestätigen:String){
    if(psw===pswbestätigen){
      this.network.CreateUser(User,psw);
    }
  }
  backtoLogin(){
    
  }
}
