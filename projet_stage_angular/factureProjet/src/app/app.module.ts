import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }   from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { Routes, RouterModule } from '@angular/router'; /*ajoute  */
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CustomersComponent } from './customers/customers.component';
import { ServicesComponent } from './services/services.component';
import { ContractsComponent } from './contracts/contracts.component';
import { OffersComponent } from './offers/offers.component';
import { BillsComponent } from './bills/bills.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  {path:"Customers", component : CustomersComponent },
  {path:"Contracts", component : ContractsComponent },
  {path:"Services", component : ServicesComponent },
  {path:"Offers", component : OffersComponent },
  {path:"Bills", component : BillsComponent },
  {path:"Login", component : LoginComponent }


];/* ... */


@NgModule({
  declarations: [
    AppComponent,
    CustomersComponent,
    ServicesComponent,
    ContractsComponent,
    OffersComponent,
    BillsComponent,
    LoginComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
      
  ],
  providers: [],                   
  bootstrap: [AppComponent]
})
export class AppModule { }
