class forexpair:
    pair_count=0
    def __init__(self,type,active_session):
        self.type=type
        self.active_session=active_session
        forexpair.pair_count+=1
pair1=forexpair('AudCad','Asian')
pair2=forexpair('AudUsd','London')
pair3=forexpair('JpyUsd','Asian')
pair4=forexpair('GbpUsd','NY')
print(forexpair.pair_count)