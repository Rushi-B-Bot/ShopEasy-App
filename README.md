 
# Note : No one can hit the other people's profile  url or there personal data just changig the url or anything so 
#        add the secuirtes for this without login that valid use cant open other ppl data or any single infomation


-- backednd start in the venv:
1) source venv/bin/activate --- venv

-- backednd stop in the venv:
2) source venv/bin/deactivate ----denv

--  run the app & start the application
3) uvicorn app.main:app --reload


1) Flow of REQ And RES
CQRS Patter  Design like use : 

----> REQ ---> FE - Validation ---> BE - Validations [before / after ] 
----> BE - Check authentication / authorization  REQ ---> BE  - Data Process[Data Security] +
----> DB ---> only shared the necessay data [ optimization ]---> 
----> BE - check  data  Reponse proper or not ----> FE- SHow the data / acess