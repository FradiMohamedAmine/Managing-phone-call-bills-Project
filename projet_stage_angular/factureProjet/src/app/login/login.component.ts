import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { Login } from '../login.model';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginresult : Login[]
  notcorrect3: boolean;
  notcorrect1: boolean;
  notcorrect2: boolean;
  constructor(private loginService : LoginService,private router: Router) { }

  ngOnInit(): void {
    
  }
  verify(f : NgForm){
    this.loginService.Check(f.value.first, f.value.last).subscribe(data =>{ 
      
      this.loginresult = data
      console.log(this.loginresult)
      console.log(this.loginresult["login"])

      if(this.loginresult["login"]== true ){
          this.router.navigate(['/Customers']);
        }
      else{
        this.router.navigate(['/Login']);

      }

      if(this.loginresult["userName"]== true ){
        this.notcorrect1 = false
      }
      else 
      this.notcorrect1 = true

      if(this.loginresult["password"]== true){        
        this.notcorrect2 = false
      }
      else{
      this.notcorrect2 = true
      }
        
  
  
    });
  
  }



}
