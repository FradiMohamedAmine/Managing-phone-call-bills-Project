import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
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


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
