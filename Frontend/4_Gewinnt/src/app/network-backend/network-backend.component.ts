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
  player1!:String;
  player2!:String;
  Token!: String;
  GameState!:String;
  Response!: String;
  GameColumn0!:Number[];
  constructor(private http: HttpClient,public router:Router, private routing:RoutingComponent) { }
  configUrl = 'http://mikepython256.pythonanywhere.com/login';

   Autherisation(User:String,psw:String) {
    const User1=JSON.parse('{ "username": "'+User+'", "password":"'+psw+'" }');
    console.log(JSON.parse('{ "username": "'+User+'", "password":"'+psw+'" }'));
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://mikepython256.pythonanywhere.com/login'
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
          this.player1 = User;
          this.GetOnline();
          this.routing.routetoMain();
        }

      })
  }
  logOut(){
    this.configUrl = 'http://mikepython256.pythonanywhere.com/logout';
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://mikepython256.pythonanywhere.com/login'
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
  fetchPlayerturn(){
    this.configUrl = 'http://mikepython256.pythonanywhere.com/state';

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://mikepython256.pythonanywhere.com/state'
    });
    let options = { headers: headers };
    const User1=JSON.parse('{ "token": "'+this.Token+'" }');
    console.log(JSON.parse('{ "token": "'+this.Token+'" }'))
    this.http.post<JSON>(this.configUrl,User1,options).subscribe(data=>{
      let jsonObj = JSON.parse(JSON.stringify(data))
      var Player = document.getElementById("Player") as HTMLLabelElement;
      if(jsonObj.player1turn==true){
        return this.player1;
      }else{
        return this.player2;
      }
      
    })
  }
  fetchGameState():boolean{
    this.configUrl = 'http://mikepython256.pythonanywhere.com/state';

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://mikepython256.pythonanywhere.com/state'
    });
    let options = { headers: headers };
    const User1=JSON.parse('{ "token": "'+this.Token+'" }');
    console.log(JSON.parse('{ "token": "'+this.Token+'" }'))
    this.http.post<JSON>(this.configUrl,User1,options).subscribe(data=>{
      let jsonObj = JSON.parse(JSON.stringify(data))
      var Player = document.getElementById("Player") as HTMLLabelElement;
      this.GameState = jsonObj.game_state;
      
    })
    return false;
  }
  GameMove(ColumnNumber:Number){
    this.configUrl = 'hhttp://mikepython256.pythonanywhere.com/move';

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://mikepython256.pythonanywhere.com/move'
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
    this.td='Column' +this.Column+'_Row'+this.Row;

    console.log(this.td)
 
    const page = window.open('vier-gewinnt-spiel.component.html')
    console.log(this.td)
    this.shand=document.getElementById(this.td);
    console.log(this.shand)
    if (this.Player===1) {
      this.shand.style.backgroundColor= "blue";
    }else if (this.Player===2){
      this.shand.style.backgroundColor= "red";
    }
  
  }
  GetOnline(){
    this.configUrl = 'http://mikepython256.pythonanywhere.com/fetch_online_users';
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://mikepython256.pythonanywhere.com/login'
    });
    
    let options = { headers: headers };
    const User1=JSON.parse('{ "token": "'+this.Token+'" }');
    console.log(User1)

    this.http.post<JSON>(this.configUrl,User1,options).subscribe(data=>{
      let list = data;
      let jsonObj=JSON.parse(JSON.stringify(data));
      let list1= jsonObj.online_player_list as string[]
      var selector = document.getElementById("OnlinePlayer") as HTMLSelectElement;
      for(let i = 0; i<list1.length;i++){
        console.log(list1[i])
        selector.options[i] = new Option(list1[i],list1[i]);
        
      }
      

      
    
    
    })


    
  }
  async getgamestateasync(){
    let gamestatebool=false;

    while(gamestatebool===false){
      gamestatebool  =  this.fetchGameState();
      console.log(this.GameState)
      console.log(this.GameState==="ongoing")
      if(this.GameState==="ongoing"){this.router.navigate(['/vier-gewinnt-spiel']);break}

        await new Promise(resolve=> setTimeout(resolve, 1000));
    }
    
  }
  RequestGame(username:String){
    this.configUrl = 'hhttp://mikepython256.pythonanywhere.com/request_game';
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://mikepython256.pythonanywhere.com/request_game'
    });
    let options = { headers: headers };
    const User1=JSON.parse('{ "token": "'+this.Token+'", "username":"'+username+'" }');
    this.player2=username;
    console.log(JSON.parse('{ "token": "'+this.Token+'", "username":"'+username+'" }'))
    this.http.post<JSON>(this.configUrl,User1,options).subscribe(data=>{
      let jsonObj = JSON.parse(JSON.stringify(data))
      console.log(jsonObj)
      if(jsonObj.status == "ok"){
        this.getgamestateasync();
        
      }
    })


  }
  CreateUser(User:String,psw:String){
    const User1=JSON.parse('{ "username": "'+User+'", "password":"'+psw+'" }');
    this.configUrl = 'http://mikepython256.pythonanywhere.com/create_user';
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
