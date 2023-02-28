# URL-Parser

Very simple URL Parser I made in 15m to parse instagram URLs and acess the URL variables and mapping more easily

## Example Input: 
https://instagram.flis8-1.fna.fbcdn.net/v/t51.2885-15/333070911_749859266424801_2188986824084027810_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.flis8-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=m6u3INmSVsIAX-gA_E5&edm=AEw_LKABAAAA&ccb=7-5&ig_cache_key=MzA0NTgyMDM5MzI4OTM4NzQ2NQ%3D%3D.2-ccb7-5&oh=00_AfBgecNqDEk-P0KkeKpLHHWn_eCMKR_b-3LSxgsnJb3mtg&oe=64017625&_nc_sid=c7f314


## Example output: 
```
Type: HTTPS

 ⤷ instagram.flis8-1.fna.fbcdn.net
  ⤷ v
   ⤷ t51.2885-15
    ⤷ 333070911_749859266424801_2188986824084027810_n.jpg

Variables: 

stp = dst-jpg_e15
_nc_ht = instagram.flis8-1.fna.fbcdn.net
_nc_cat = 109
_nc_ohc = m6u3INmSVsIAX-gA_E5
edm = AEw_LKABAAAA
ccb = 7-5
ig_cache_key = MzA0NTgyMDM5MzI4OTM4NzQ2NQ%3D%3D.2-ccb7-5
oh = 00_AfBgecNqDEk-P0KkeKpLHHWn_eCMKR_b-3LSxgsnJb3mtg
oe = 64017625
_nc_sid = c7f314

Process finished with exit code 0

```
