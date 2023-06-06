import { Component } from '@angular/core';
import { Router } from '@angular/router';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'factureProjet';


  
  constructor(private router: Router 
    ) {}

  ngOnInit(): void {
 //   this.router.navigate(['/Login'])

  }
  logout() {

    this.router.navigate(['/login']);
}


}

