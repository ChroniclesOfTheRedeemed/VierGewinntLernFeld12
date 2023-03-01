import { Component,Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-network-backend',
  templateUrl: './network-backend.component.html',
  styleUrls: ['./network-backend.component.css']
})

@Injectable({ providedIn:'any' })
export class NetworkBackendComponent {
  bool: any;
  corsHeaders: HttpHeaders = new HttpHeaders;
  root!: string;

  constructor(private http: HttpClient) { }
  configUrl = 'http://127.0.0.1:5000/login';

  public Autherisation(User:JSON) {
    this.root = 'http://localhost:5000';  //remove
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Access-Control-Allow-Origin': 'http://localhost:5000/Login',  // edit 
      responseType: 'json'
    });
    let options = { headers: headers };
    this.http.post(this.configUrl,User,{responseType: 'json'}).subscribe(data=>{
      this.bool = data;console.log(this.bool)
    }
      
       
    )   
    return this.bool;
  }
}
