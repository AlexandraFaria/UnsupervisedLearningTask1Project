#%%
# Inverse transform data to verify encoding and return back to original data frame format prior to OneHotEncoding, MultiLabelBinarizer, and OrdinalEncoder

# Inverse Transform One_Hot_Encoded Data
data = pd.concat([data.drop(columns=one_hot_data.columns), pd.DataFrame(encoder.inverse_transform(one_hot_data), columns=categorical_columns)], axis=1)

# Inverse Transform OrdinalEncoded Data
data = pd.concat([data.drop(columns=list(ordinal_features_categories.keys())), pd.DataFrame(ordinal_encoder.inverse_transform(ordinal_encoded), columns=list(ordinal_features_categories.keys()))], axis=1)

# Inverse transform MultiLabelBinarizer Rows and concatenate with original data set.

decoded_multi_data = one_hot_multiclass.inverse_transform(data[one_hot_multiclass.classes_].values)
data['work_position'] = ['|'.join(category) for category in decoded_multi_data]
data = data.drop(columns=one_hot_multiclass.classes_)

data.head()