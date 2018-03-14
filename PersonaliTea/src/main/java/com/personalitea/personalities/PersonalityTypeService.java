package com.personalitea.personalities;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by nathanjekel on 2/1/18.
 */
public class PersonalityTypeService {

    private static List<PersonalityType> personalityTypeList = new ArrayList<PersonalityType>();
    static {
        personalityTypeList.add(new PersonalityType("ESTJ"));
        personalityTypeList.add(new PersonalityType("ESFJ"));
        personalityTypeList.add(new PersonalityType("ISTJ"));
        personalityTypeList.add(new PersonalityType("ISFJ"));
    }

    public List<PersonalityType> getPersonalityTypeList() {
        return personalityTypeList;
    }

    public void addPersonalityType(PersonalityType personalityType) {
        personalityTypeList.add(personalityType);
    }

    public void deletePersonalityType(PersonalityType personalityType) {
        personalityTypeList.remove(personalityType);
    }


}
