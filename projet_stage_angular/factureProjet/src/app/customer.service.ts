import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError, map } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';
import { pipe } from 'rxjs';
import { Customer1 } from './customer1.model';



@Injectable({
  providedIn: 'root' , 

  
})


export class CustomerService  {



  
  
  constructor(private _http : HttpClient ) { }


  onSearch() : Observable<Customer1[]> {
  let url = `http://127.0.0.1:8000/api/clientlist/`
    return this._http.get<any>(url) ; 
    
  } 
 
  


  onSearch2(dataForm) : Observable<Customer1[]> {
    let url = `http://127.0.0.1:8000/api/clientdetail/${dataForm}/`
      return this._http.get<any>(url) ; 
      
    } ;



   
}  
   

      
     
