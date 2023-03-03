import { Component,Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, retry, timeout } from 'rxjs';
import { Router, Routes } from '@angular/router';
import { MainPageComponent } from '../main-page/main-page.component';
import { RoutingComponent } from '../routing/routing.component';
import { ArrayType } from '@angular/compiler';
@Component({
  selector: 'app-network-backend',
  templateUrl: './network-backend.component.html',
  styleUrls: ['./network-backend.component.css']
})

@Injectable({ providedIn:'any' })
export class NetworkBackendComponent {
  bool: any="";
  corsHeaders: HttpHeaders = new HttpHeaders;
  root!: string;
  testjson!: JSON;
  Token!: String;
  Response!: String;
  GameColumn0!:Number[];
  constructor(private http: HttpClient,public router:Router, private routing:RoutingComponent) { }
  configUrl = 'http://127.0.0.1:5000/login';

   Autherisation(User:String,psw:String) {
    const User1=JSON.parse('{ "username": "'+User+'", "password":"'+psw+'" }');
    console.log(JSON.parse('{ "username": "'+User+'", "password":"'+psw+'" }'));
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://localhost:5000/login'
    });
    let options = { headers: headers };
    
      this.http.post<JSON>(this.configUrl,User1).subscribe(data=>{
      let jsonObj = JSON.parse(JSON.stringify(data))
    
        console.log("status: " + jsonObj.status + ", token: " + jsonObj.token)
        if (jsonObj.status === "invalid"){

        }else if(jsonObj.status  === "Bad Request"){
    
        }else if (jsonObj.status !== undefined&&  typeof jsonObj.status === 'string'){
          this.Response=jsonObj.status;
        }
        if(jsonObj.token !== 0&&  typeof jsonObj.token  === 'string'){
          this.Token=jsonObj.token;
          console.log(jsonObj.token)
          
        }
        if(this.Token!=="0" && this.Response==="ok"){
          this.routing.routetoMain();
        }

      })
  }
  logOut(){
    this.configUrl = 'http://127.0.0.1:5000/logout';
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://localhost:5000/login'
    });
    let options = { headers: headers };
    const User1=JSON.parse('{ "token": "'+this.Token+'" }');
    this.http.post<JSON>(this.configUrl,User1,options).subscribe(data=>{
      let jsonObj = JSON.parse(JSON.stringify(data))
      console.log(jsonObj.status+":status")
      console.log(this.Token+":Token")
      if (jsonObj.status  === "bad request"){

      }else if (jsonObj.status  === "ok"){
        this.Token="";
        this.router.navigate(['/'])
      }
      console.log(jsonObj.status+":status")
      console.log(this.Token+":Token")
    })
  }
  GameMove(ColumnNumber:Number){
    this.configUrl = 'http://127.0.0.1:5000/move';

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://localhost:5000/login'
    });
    let options = { headers: headers };
    const User1=JSON.parse('{ "token": "'+this.Token+'", "coloumnNumber":'+ColumnNumber+' }');
    console.log(JSON.parse('{ "token": "'+this.Token+'", "coloumnNumber":'+ColumnNumber+' }'))
    this.http.post<JSON>(this.configUrl,User1,options).subscribe(data=>{
      console.log(data)
      let jsonObj = JSON.parse(JSON.stringify(data))
    console.log(jsonObj.game_field.coloumn_0[0] +"column1")
    for(let i = 0; i < 6; i++){
      if(jsonObj.game_field.coloumn_0[i]===1){
        
        this.Backgroundcolour(new Array (1,0,i));
        
      }else if (jsonObj.game_field.coloumn_0[i]===2){
        this.Backgroundcolour(new Array (2,0,i));
      }
      if(jsonObj.game_field.coloumn_1[i]===1){
        this.Backgroundcolour(new Array (1,1,i));
      }else if (jsonObj.game_field.coloumn_1[i]===2){
        this.Backgroundcolour(new Array (2,1,i));
      }
      if (jsonObj.game_field.coloumn_2[i]===1){
        this.Backgroundcolour(new Array (1,2,i));
        
      }else if (jsonObj.game_field.coloumn_2[i]===2){
        this.Backgroundcolour(new Array (2,2,i));
      }
      if(jsonObj.game_field.coloumn_3[i]===1){
        this.Backgroundcolour(new Array (1,3,i));
        
      }else if (jsonObj.game_field.coloumn_3[i]===2){
        this.Backgroundcolour(new Array (2,3,i));
      }
      if (jsonObj.game_field.coloumn_4[i]===1){
        this.Backgroundcolour(new Array (1,4,i));
      }else if (jsonObj.game_field.coloumn_4[i]===2){
        this.Backgroundcolour(new Array (2,4,i));
      }
      if(jsonObj.game_field.coloumn_5[i]===1){
        this.Backgroundcolour(new Array (1,5,i));
      }else if (jsonObj.game_field.coloumn_5[i]===2){
        this.Backgroundcolour(new Array (2,5,i));
      }
      if (jsonObj.game_field.coloumn_6[i]===1){
        this.Backgroundcolour(new Array (1,6,i));
        
      }else if (jsonObj.game_field.coloumn_6[i]===2){
        this.Backgroundcolour(new Array (2,6,i));
      }
      console.log(jsonObj.game_field.coloumn_0[i]+"column1"+i)
      console.log(jsonObj.game_field.coloumn_1[i]+"column2"+i)
      console.log(jsonObj.game_field.coloumn_2[i]+"column3"+i)
      console.log(jsonObj.game_field.coloumn_3[i]+"column4"+i)
      console.log(jsonObj.game_field.coloumn_4[i]+"column5"+i)
      console.log(jsonObj.game_field.coloumn_5[i]+"column6"+i)
      console.log(jsonObj.game_field.coloumn_6[i]+"column7"+i)

    }
return null;
    })
  }
  td!: string;
  Player!: Number;
  Column!: Number;
  Row!: Number;
  
  shand:any = document.getElementById(this.td);
  Backgroundcolour(numberArrray:Number[]){
    console.log("Backgound is working")
    if(numberArrray[0]===1){
      this.Player=1;
    }else if (numberArrray[0]===2){
      this.Player=2;
    }
    for(let i = 0; i < 7; i++){
      if(numberArrray[1]===i){
        this.Column=i;
      }
    }
    for(let i = 0; i < 6; i++){
      if(numberArrray[2]===i){
        this.Row=i;
      }
    }
    this.td="Column" +this.Column+"_Row"+this.Row;

    console.log(this.td)
 
    const page = window.open('vier-gewinnt-spiel.component.html')
    this.shand=page?.document.getElementById(this.td);
    if (this.Player===1) {
      this.shand.style.backgroundColor= "blue";
    }else if (this.Player===2){
      this.shand.style.backgroundColor= "red";
    }
  
  }
  RequestGame(match_type:String){
    this.configUrl = 'http://127.0.0.1:5000/request_game';
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://localhost:5000/login'
    });
    let options = { headers: headers };
    const User1=JSON.parse('{ "token": "'+this.Token+'", "match_type":"'+match_type+'" }');
    console.log(JSON.parse('{ "token": "'+this.Token+'", "match_type":"'+match_type+'" }'))
    this.http.post<JSON>(this.configUrl,User1,options).subscribe(data=>{
      let jsonObj = JSON.parse(JSON.stringify(data))
    console.log(jsonObj.game_field.coloumn_0[1]+"column1")
      for(let i = 0; i < 6; i++){
        console.log(jsonObj.game_field.coloumn_0[i]+"column1"+i)
        console.log(jsonObj.game_field.coloumn_1[i]+"column2"+i)
        console.log(jsonObj.game_field.coloumn_2[i]+"column3"+i)
        console.log(jsonObj.game_field.coloumn_3[i]+"column4"+i)
        console.log(jsonObj.game_field.coloumn_4[i]+"column5"+i)
        console.log(jsonObj.game_field.coloumn_5[i]+"column6"+i)
        console.log(jsonObj.game_field.coloumn_6[i]+"column7"+i)

      }
   

    })
  }
  CreateUser(User:String,psw:String){
    const User1=JSON.parse('{ "username": "'+User+'", "password":"'+psw+'" }');
    this.configUrl = 'http://127.0.0.1:5000/create_user';
    this.http.post<JSON>(this.configUrl,User1).subscribe(data=>{
      console.log(""+JSON.stringify(data) )
      let jsonObj = JSON.parse(JSON.stringify(data))
    
        console.log("token: " + jsonObj.token + ", status: " + jsonObj.status)
        if (jsonObj.status === "invalid"){

        }else if(jsonObj.status  === "Bad Request"){
    
        }else if (jsonObj.status !== undefined&&  typeof jsonObj.status === 'string'){
          this.Response=jsonObj.status;
        }
        if(jsonObj.token !== 0&&  typeof jsonObj.token  === 'number'){
          this.Token=jsonObj.token;
          console.log(this.Token)
        }else if (jsonObj.token  === "User already exists"){

        }
   
      console.log(Number.parseFloat(jsonObj.token))
      console.log(typeof jsonObj.token  === 'number')
      console.log(jsonObj.token !== 0)
      console.log(this.Response)
      if(this.Token!=="0" && this.Response==="ok"){
        this.router.navigate(['/Main-Page']);
        console.log(this.bool,"test")
      }

    })
  }
}
